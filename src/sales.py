import json
import os
import requests
import random
import time
import spacy
import argparse
from typing import List, Union
from spacy.tokens import Span, Doc
from tqdm.auto import tqdm
import pandas as pd
import warnings
from src.base import Base

warnings.filterwarnings("ignore", category=UserWarning)
tqdm.pandas()


class Sales(Base):
    def __init__(self, headers: str = "", cookies: str = ""):
        """
        Args:
            headers (str): path to the headers.json file
            cookies (str): path to the cookies.json file
        """
        super().__init__(headers, cookies)
        self.nlp = spacy.load("en_core_web_md")

    def words_to_spans(self, words):
        """
        Converts a list of words to a list of spaCy spans
        Args:
            words (list): a list of words
        Returns:
            list: a list of spaCy spans
        """
        spans = []
        for word in words:
            doc = self.nlp(word)
            spans.append(doc[0:1])
        return spans

    def compare_tokens(self, span1: Union[Span, Doc], span2: Union[Span, Doc]):
        """
        Compares two spaCy span
        Args:
            span1 (spacy.tokens.span.Span): a spaCy span
            span2 (spacy.tokens.span.Span): a spaCy span
        Returns:
            bool: True if the spans are the same, False otherwise
        """

        ## check word by word
        for token1 in span1:
            for token2 in span2:
                if token1.text.lower() == token2.text.lower():
                    return True
                elif token1.lemma_.lower() == token2.lemma_.lower():
                    return True
        ## check if the spans are similar

        if isinstance(span1, Span) and isinstance(span2, Span):
            ## get all the noun chunks
            span1 = [chunk for chunk in span1.noun_chunks]
            span1 = [chunk for chunk in span1 if chunk.root.dep_ == "nsubj"]
            span2 = [chunk for chunk in span2.noun_chunks]
            span2 = [chunk for chunk in span2 if chunk.root.dep_ == "nsubj"]
            ## check if the spans are similar
            for chunk1 in span1:
                for chunk2 in span2:
                    if chunk1.similarity(chunk2) > 0.8:
                        return True

        if isinstance(span1, Doc):
            ## get all the noun chunks
            span1 = [chunk for chunk in span1.noun_chunks]
            span1 = [chunk for chunk in span1 if chunk.root.dep_ == "nsubj"]
            ## check if the spans are similar
            for chunk in span1:
                if chunk.similarity(span2) > 0.8:
                    return True
        elif isinstance(span2, Doc):
            ## get all the noun chunks
            span2 = [chunk for chunk in span2.noun_chunks]
            span2 = [chunk for chunk in span2 if chunk.root.dep_ == "nsubj"]
            ## check if the spans are similar
            for chunk in span2:
                if chunk.similarity(span1) > 0.8:
                    return True

        return False

    def rankify(self, row, included_words: List[Span], excluded_words: List[Span]):
        """
        An algorithm to rank leads based on their attributes
        Args:
            row (dict): a lead
        """
        weight = 0
        ## Added minor weight for if they have premium
        if row["premium"]:
            weight += 0.15
        ## Added weight for the degree of connection, the closer th better
        weight += 1 / (row["degree"] + 1)
        desc = row["summary"]
        ## Added weight for if they have a description
        if not desc:
            weight -= 0.5
        ## check if description is written in first person
        doc = self.nlp(desc)
        for token in doc:
            if (
                token.pos_ == "PRON"
                and token.text == "I"
                or token.text.lower() == "me"
                or token.text.lower() == "my"
            ):
                weight += 0.5
                break

        # check if description contains excluded words
        for word in excluded_words:
            if self.compare_tokens(word, doc):
                weight -= 1
                break

        # check if description contains included words
        for word in included_words:

            if self.compare_tokens(word, doc):
                weight += 0.25
                break

        positions = row["currentPositions"]
        if positions:
            for pos in positions:
                title = pos.get("title", "").lower()
                company = pos.get("company", "").lower()
                industry = (
                    pos.get("companyUrnResolutionResult", {})
                    .get("industry", "")
                    .lower()
                )
                if not title or not company or not industry:
                    continue
                doc_title = self.nlp(title)
                doc_company = self.nlp(company)
                doc_industry = self.nlp(industry)
                for word in excluded_words:
                    if (
                        self.compare_tokens(doc_title, word)
                        or self.compare_tokens(doc_company, word)
                        or self.compare_tokens(doc_industry, word)
                    ):
                        weight -= 1
                        break

                for word in included_words:
                    if (
                        self.compare_tokens(doc_title, word)
                        or self.compare_tokens(doc_company, word)
                        or self.compare_tokens(doc_industry, word)
                    ):
                        weight += 0.25
                        break

        if not row["profilePictureDisplayImage"]:
            weight -= 0.3

        return weight

    def rank_leads(
        self,
        leads: pd.DataFrame,
        included_words: List[Span],
        excluded_words: List[Span],
    ):
        """
        Ranks leads based on their attributes
        Args:
            leads (list): a list of leads
            included_words (list): a list of spaCy spans
            excluded_words (list): a list of spaCy spans
        Returns:
            list: a list of ranked leads
        """
        leads.loc[:, ("rank")] = leads.progress_apply(
            lambda row: self.rankify(row, included_words, excluded_words), axis=1
        )
        return leads.sort_values(by="rank", ascending=False)

    def connect(self, profile_urn, message: str = ""):
        params = {
            "action": "connectV2",
        }

        data = {"member": profile_urn, "message": message}
        if not data['message']:
            del data['message']
        
        data = json.dumps(data)
        
        response = requests.post(
            "https://www.linkedin.com/sales-api/salesApiConnection",
            params=params,
            cookies=self.cookies,
            headers=self.headers,
            data=data,
        )

        if response.status_code == 200:
            return True
        else:
            print("Error connecting to lead: ", response.text)
            return False

    def save_connections(self, file_path: str):
        """
        Saves all the connections to a file
        Args:
            file_path (str): the path to the file
        """
        if not self.filtered_leads:
            print("No leads to save")
            return
        df = pd.DataFrame(self.filtered_leads)
        df = df[["fullName", "entityUrn"]]
        df.to_csv(file_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")
    connect_parser = subparsers.add_parser("connect", help="Connect to a lead.")
    rank_parser = subparsers.add_parser(
        "rank", help="Rank our leads based on their attributes."
    )
    find_parser = subparsers.add_parser(
        "find", help="Find all our leads and save them to a file."
    )

    rank_parser.add_argument("--included", type=str, help="path to included words")
    rank_parser.add_argument("--excluded", type=str, help="path to excluded words")
    rank_parser.add_argument("--leads", type=str, required=True, help="path to leads")

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
    find_parser.add_argument(
        "--identity",
        type=str,
        required=True,
        help="The identity for the profile you want to use. Must be a directory with headers and cookies.json.",
    )

    connect_parser.add_argument(
        "--leads", type=str, required=True, help="path to leads"
    )
    connect_parser.add_argument(
        "--identity",
        type=str,
        required=True,
        help="The identity for the profile you want to use. Must be a directory with headers and cookies.json.",
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
        "--message",
        type=str,
        help="The message to send to the leads. Could be a file or a string. If a file, it must be a txt file. It can use {name} and {person} to insert the name and person of the lead.",
        default="",
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
        "--max_connections",
        type=int,
        default=50,
        help="The max number of connections to send out.",
    )

    args = parser.parse_args()

    # check lead file extension
    if args.leads.endswith(".json"):
        leads = pd.read_json(args.leads)
    elif args.leads.endswith(".csv"):
        leads = pd.read_csv(args.leads)
    else:
        raise Exception("Invalid file extension")

    sales = Sales()

    if args.command == "rank":
        if args.included:
            included_words = (
                open(args.included, "r", encoding="utf-8").read().splitlines()
            )
        else:
            included_words = []
        if args.excluded:
            excluded_words = (
                open(args.excluded, "r", encoding="utf-8").read().splitlines()
            )
        else:
            excluded_words = []

        included_words = sales.words_to_spans(included_words)
        excluded_words = sales.words_to_spans(excluded_words)

        ## remove pending invitations
        leads = leads[leads["pendingInvitation"] == False]
        leads = leads.fillna("")
        leads = sales.rank_leads(leads, included_words, excluded_words)
        leads_file = args.leads.replace(".json", "_ranked.json")
        leads.to_json(leads_file, orient="records", indent=4)
        print("Saved to", f"{args.leads}_ranked.json")

    elif args.command == "find":
        header_file = args.identity + "/headers.json"
        cookie_file = args.identity + "/cookies.json"
        sales.load_headers(header_file)
        sales.load_cookies(cookie_file)
        sales.get_leads(
            args.url,
            args.start,
            args.count,
            args.end,
            args.output,
            time_delay_max=args.delay,
        )

    elif args.command == "connect":
        header_file = args.identity + "/headers.json"
        cookie_file = args.identity + "/cookies.json"
        sales.load_headers(header_file)
        sales.load_cookies(cookie_file)

        if args.message:
            if os.path.exists(args.message):
                with open(args.message, "r", encoding="utf-8") as f:
                    args.message = f.read()
        # check lead file extension
        if args.leads.endswith(".json"):
            leads = pd.read_json(args.leads)
        elif args.leads.endswith(".csv"):
            leads = pd.read_csv(args.leads)
        else:
            raise Exception("Invalid file extension")

        if os.path.exists(args.connect_file):
            ## load the existing connections
            connections = pd.read_csv(args.connect_file)
            ## remove the connections that have already been made

            leads = leads[~leads["entityUrn"].isin(connections["entityUrn"])]
            leads.reset_index(inplace=True, drop=True)
            sales.filtered_leads = connections.to_dict("records")

        # load connections
        for idx, row in leads.iterrows():
            try:
                first_name = row["firstName"]
                message = sales.create_message(args.message, first_name, args.person)
                print(idx, "Sending message to", row["firstName"], row["lastName"])
                print('Message: "', message, '"')
                entity_urn = row["entityUrn"]

                ## regex all content between brackets not including the brackets
                entity_id = entity_urn[entity_urn.find("(") + 1 : entity_urn.find(")")]
                profile_id = entity_id.split(",")[0]
                
                ## send the connection request	
                if sales.connect(profile_id, message):
                    ## save the connection
                    row['status'] = 'success'
                    print("Connected to", row["firstName"], row["lastName"])
                else:
                    row['status'] = 'failure'
                sales.filtered_leads.append(row)

                ## wait for a random amount of time
                delay = random.randint(args.send_delay_min, args.send_delay_max)
                print("Waiting for", delay, "seconds")
                time.sleep(delay)

            except KeyboardInterrupt:
                break

            except Exception as e:
                print("Error:", e)
                continue
            finally:
                if idx >= args.max_connections:
                    break
        ## save the connections
        sales.save_connections(args.connect_file)
