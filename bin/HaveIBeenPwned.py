#! /usr//bin/python3
#
#  author:        Kamonabe
#  First edition: Sep 25, 2019
#  Last Update:   Sep 25, 2019
#  Free to use
#  Free to modify

import argparse
import configparser
import requests
import pprint
import sys


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--breach", help="Getting all breaches for an account.")
args = parser.parse_args()


config = configparser.ConfigParser()
config.read("/usr/local/hibp/etc/hibp.ini")


class HaveIBeenPwned:
    def __init__(self):
        self.baseUrl = "https://haveibeenpwned.com/api/v3/"
        self.headers = {}
        self.headers["content-type"] = "application/json"
        self.headers["api-version"] = "3"
        self.headers["User-Agent"] = "the-monkey-playground-script"
        self.headers["hibp-api-key"] = config["Api"]["key"]  # Paste the API key.

    def breachesAnAccount(self, account):
        apiUrl = "{}breachedaccount/{}?truncateResponse=false".format(
            self.baseUrl, account
        )
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            print("[*] Warning; Breach Check for: {}".format(account))
            for data in resp.json():
                print("=========================")
                print("  - Name: {}".format(data["Name"]))
                print("  - Title: {}".format(data["Title"]))
                print("  - Domain: {}".format(data["Domain"]))
                print("  - BreachDate: {}".format(data["BreachDate"]))
                print("  - AddedDate: {}".format(data["AddedDate"]))
                print("  - ModifiedDate: {}".format(data["ModifiedDate"]))
                print("  - PwnCount: {}".format(data["PwnCount"]))
                print("  - Description:\n{}".format(data["Description"]))
                print("  - DataClasses: {}".format(", ".join(data["DataClasses"])))
                print("  - IsVerified: {}".format(data["IsVerified"]))
                print("  - IsFabricated: {}".format(data["IsFabricated"]))
                print("  - IsSensitive: {}".format(data["IsSensitive"]))
                print("  - IsRetired: {}".format(data["IsRetired"]))
                print("  - IsSpamList: {}".format(data["IsSpamList"]))
                print("  - LogoPath: {}".format(data["LogoPath"]))
        elif resp.status_code == 404:
            print("[*] Info; {} not found in a breach".format(account))


if __name__ == "__main__":
    classhibp = HaveIBeenPwned()

    if args.breach is not None:
        classhibp.breachesAnAccount(args.breach)
