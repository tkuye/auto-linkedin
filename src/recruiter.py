import sys
import requests
import json
import argparse
import time
import random
import os
import csv

from src.base import Base


class MessageError(Exception):
    pass


class Recruiter(Base):
    def __init__(self, headers_file, cookies_file):
        super().__init__(headers_file, cookies_file)
        self.filtered_leads = []
        self.valid_connections = []

    def get_profile(self, profile_id: str) -> dict:

        params = {
            "q": "memberIdentity",
            "memberIdentity": profile_id,
            "decorationId": "com.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore-16",
        }

        response = requests.get(
            "https://www.linkedin.com/voyager/api/identity/dash/profiles",
            params=params,
            cookies=self.cookies,
            headers=self.headers,
        )
        status = response.status_code
        if status == 200:
            return response.json()
        else:
            print(f"Error: {status} {response.text}")
            return {}

    def connect(self, profile_urn, message: str = ""):
        params = {
            "action": "verifyQuotaAndCreate",
            "decorationId": "com.linkedin.voyager.dash.deco.relationships.InvitationCreationResult-3",
        }

        json_data = {
            "inviteeProfileUrn": profile_urn,
            "customMessage": message,
        }
        if message == "":
            del json_data["customMessage"]

        response = requests.post(
            "https://www.linkedin.com/voyager/api/voyagerRelationshipsDashMemberRelationships",
            params=params,
            cookies=self.cookies,
            headers=self.headers,
            json=json_data,
        )
        status = response.status_code
        if status == 200:
            print(f"Connected to {profile_urn}")
            return response.json()
        elif status == 500:
            ## Linkedin is weird and sometimes returns 500 for no reason but still connects
            print(f"Connected to {profile_urn}")
            return response.json()
        else:
            print(f"Error: {status} {response.text}")
            return {}

    def get_profile_and_connect(self, profile_id, message: str = ""):
        profile = self.get_profile(profile_id)
        profile_urn = profile.get("data", {}).get("*elements", [""])[0]
        if profile_urn:
            time.sleep(random.randint(3, 6))
            response = self.connect(profile_urn, message)
            return response

    def get_lead_data_filtered(self, data: list):
        outdata = []
        for lead in data:
            first_name = lead.get("linkedInMemberProfileUrnResolutionResult", {}).get(
                "unobfuscatedFirstName"
            )
            last_name = lead.get("linkedInMemberProfileUrnResolutionResult", {}).get(
                "unobfuscatedLastName"
            )
            if not first_name:
                first_name = lead.get(
                    "linkedInMemberProfileUrnResolutionResult", {}
                ).get("firstName")
            if not last_name:
                last_name = lead.get(
                    "linkedInMemberProfileUrnResolutionResult", {}
                ).get("lastName")

            profile_url = lead.get("linkedInMemberProfileUrnResolutionResult", {}).get(
                "publicProfileUrl", ""
            )
            if profile_url:
                profile_id = profile_url.split("/in/")[1]
            else:
                profile_id = None

            if first_name and last_name and profile_id:
                outdata.append(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "profile_id": profile_id,
                    }
                )

        print(f"Filtered leads: {len(outdata)}")
        self.filtered_leads = outdata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--identity",
        type=str,
        required=True,
        help="The identity for the profile you want to use. Must be a directory with headers and cookies.json.",
    )

    subparsers = parser.add_subparsers(
        help="Type of recruiter to use.", dest="recruiter_type"
    )
    connect_parser = subparsers.add_parser("connect", help="Connect to leads")
    connect_parser.add_argument(
        "--leads", type=str, required=True, help="The leads file to use."
    )
    connect_parser.add_argument(
        "--message",
        type=str,
        help="The message to send to the leads. Could be a file or a string. If a file, it must be a txt file. It can use {name} and {person} to insert the name and person of the lead.",
        default="Hi {name}, I saw your profile and I think you would be a great fit for our team. I would love to connect and discuss how we can work together. Let me know if you are interested. Thanks!",
    )
    connect_parser.add_argument(
        "--connect_file",
        type=str,
        default="connections.csv",
        help="The file name to save the valid connections to.",
    )
    connect_parser.add_argument(
        "--person",
        type=str,
        help="The person sending the message. Used in the '{person}' field of the outgoing message.",
    )
    connect_parser.add_argument(
        "--send_delay_min",
        type=int,
        default=120,
        help="The minimum range for the delay for sending connect requests.",
    )
    connect_parser.add_argument(
        "--send_delay_max",
        type=int,
        default=180,
        help="The maximum range for the delay for sending connect requests.",
    )
    connect_parser.add_argument(
        "--max_connections",
        type=int,
        default=50,
        help="The max number of connections to send out.",
    )

    find_parser = subparsers.add_parser(
        "find", help="Find all our leads and save them to a file."
    )
    find_parser.add_argument(
        "--url",
        type=str,
        required=True,
        help="The url to use to find leads. (ex: https://www.linkedin.com/sales-api/salesApiSearch?start=0&count=25&searchId=...)",
    )
    find_parser.add_argument(
        "-s", "--start", type=int, default=0, help="The start index for the search."
    )
    find_parser.add_argument(
        "-c", "--count", type=int, default=25, help="The count per page."
    )
    find_parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=1000,
        help="The end index for the search. (Max number of leads to find)",
    )
    find_parser.add_argument(
        "-o", "--output", type=str, default="leads.json", help="path to output file"
    )
    find_parser.add_argument(
        "-d", "--delay", type=int, default=5, help="time delay between requests"
    )

    args = parser.parse_args()

    identity = args.identity

    if not os.path.exists(identity):
        print(f"Identity {identity} does not exist")
        sys.exit(1)

    recruiter = Recruiter(
        cookies_file=identity + "/cookies.json", headers_file=identity + "/headers.json"
    )

    if args.recruiter_type == "connect":
        if args.message:
            if os.path.exists(args.message):
                with open(args.message, "r", encoding="utf-8") as f:
                    args.message = f.read()

        if not os.path.exists(args.leads):
            print(f"Leads file {args.leads} does not exist")
            sys.exit(1)
        with open(args.leads, "r", encoding="utf-8") as f:
            leads = json.load(f)
        recruiter.get_lead_data_filtered(leads)
        for lead in recruiter.filtered_leads:
            try:
                print(f'Connecting to {lead["first_name"]} {lead["last_name"]}...')
                res = recruiter.get_profile_and_connect(
                    lead["profile_id"],
                    recruiter.create_message(
                        args.message, lead["first_name"], args.person
                    ),
                )
                if res:
                    recruiter.valid_connections.append(lead)
                if len(recruiter.valid_connections) >= args.max_connections:
                    break
                delay = random.randint(args.send_delay_min, args.send_delay_max)
                print(f"Waiting for {delay} seconds...")
                time.sleep(delay)
            except KeyboardInterrupt:
                break
        if recruiter.valid_connections:
            print("Writing valid connections to file...")
            writer = csv.DictWriter(
                open(args.connect_file, "w", encoding="utf-8"),
                fieldnames=["first_name", "last_name", "profile_id"],
            )
            writer.writeheader()
            writer.writerows(recruiter.valid_connections)

    elif args.recruiter_type == "find":
        recruiter.get_leads(
            args.url, args.start, args.count, args.end, args.output, args.delay
        )