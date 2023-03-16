import shutil
import sys
import requests
import json
import argparse
import time
import random
import os
import csv
import pandas as pd
from src.base import Base


class MessageError(Exception):
    pass


class Recruiter(Base):
    def __init__(self, headers_file=None, cookies_file=None, credentials_file=None):
        super().__init__(credentials_file, headers_file, cookies_file)
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
            timeout=10,
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

    def get_lead_data_filtered(self, data: list, existing_connections:set=None):
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
                if existing_connections and profile_id in existing_connections:
                    print(f"Skipping {profile_id} because it is already connected")
                    continue
                outdata.append(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "profile_id": profile_id,
                    }
                )
        ## remove duplicates
        outdata = [dict(t) for t in {tuple(d.items()) for d in outdata}]
        print(f"Filtered leads: {len(outdata)}")
        self.filtered_leads = outdata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
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

    connect_parser.add_argument(
        "--identity",
        type=str,
        default="",
        help="The identity for the profile you want to use. Must be a directory with headers and cookies.json.",
    )

    connect_parser.add_argument(
        "--identity_file",
        type=str,
        default="",
        help="The identity file for the profile you want to use.",
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
        "--delay_min", type=int, default=3, help="time delay between requests"
    )

    find_parser.add_argument(
        "--delay_max", type=int, default=5, help="time delay between requests"
    )

    find_parser.add_argument(
        "--identity",
        type=str,
        default="",
        help="The identity for the profile you want to use. Must be a directory with headers and cookies.json.",
    )

    find_parser.add_argument(
        "--identity_file",
        type=str,
        default="",
        help="The identity file for the profile you want to use.",
    )

    args = parser.parse_args()

    identity = args.identity
    identity_file = args.identity_file

    if not os.path.exists(identity) and not os.path.exists(identity_file):
        print(f"Identity does not exist")
        sys.exit(1)

    recruiter = Recruiter(
        cookies_file=identity + "/cookies.json", 
        headers_file=identity + "/headers.json",
        credentials_file=identity_file
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

        connect_exist = False
        if os.path.exists(args.connect_file):
            if args.connect_file.endswith(".csv"):
                df = pd.read_csv(args.connect_file)
            elif args.connect_file.endswith(".json"):
                df = pd.read_json(args.connect_file)
            else:
                raise Exception("Invalid file type")
            
            connect_exist = True
        
            existing_connections = set(df["profile_id"].values)
        else:
            existing_connections = set()
        recruiter.get_lead_data_filtered(leads, existing_connections)
        count = 0
        for lead in recruiter.filtered_leads:
            try:
                print(f'Connecting to {lead["first_name"]} {lead["last_name"]}...')
                print(f"Sending message: '{recruiter.create_message(args.message, lead['first_name'], args.person)}'")
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
            finally:
                count += 1

        if recruiter.valid_connections:
            print("Writing valid connections to file...")
            if connect_exist:
                writer = csv.DictWriter(
                    open(args.connect_file, "a", encoding="utf-8"),
                    fieldnames=["first_name", "last_name", "profile_id"],
                )
                writer.writerows(recruiter.valid_connections)
            else:
                writer = csv.DictWriter(
                    open(args.connect_file, "w", encoding="utf-8"),
                    fieldnames=["first_name", "last_name", "profile_id"],
                )
                writer.writeheader()
                writer.writerows(recruiter.valid_connections)
        if count + len(existing_connections) == len(recruiter.filtered_leads):
            print("All leads have been processed")
            ## move leads file to done folder
            ## get the file path without the file name
            path = os.path.dirname(args.leads)
            ## add done folder to the path
            path = os.path.join(path, "done")
            ## create the done folder if it does not exist
            if not os.path.exists(path):
                os.makedirs(path)
            ## move the leads file to the done folder
            shutil.move(args.leads, path)


    elif args.recruiter_type == "find":
        recruiter.get_leads(
            args.url, args.start, args.count, args.end, args.output, args.delay_min, args.delay_max
        )
