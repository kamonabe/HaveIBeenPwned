#! /usr//bin/python3
#
#  author       : Kamonabe
#  First edition: Sep 25, 2019
#  Last Update  : Sep 25, 2019
#
#  Free to use
#  Free to modify

import argparse
import configparser
import hashlib

import requests


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--breach", help="Getting all breaches for an account.")
parser.add_argument(
    "-a",
    "--allbreaches",
    action="store_true",
    help="Getting all breached sites in the system.",
)
parser.add_argument("-s", "--site", help="Getting a single breached site.")
parser.add_argument(
    "-d",
    "--dataclasses",
    action="store_true",
    help="Getting all data classes in the system.",
)
parser.add_argument("-p", "--paste", help="Getting all pastes for an account.")
parser.add_argument("-w", "--watchword", help="Searching by range.")
args = parser.parse_args()


config = configparser.ConfigParser()
config.read("/usr/local/hibp/etc/hibp.ini")


class HaveIBeenPwned:
    def __init__(self):
        self.baseUrl1 = "https://haveibeenpwned.com/api/v3"
        self.baseUrl2 = "https://api.pwnedpasswords.com"
        self.headers = {
            "content-type": "application/json",
            "api-version": "3",
            "User-Agent": "the-monkey-playground-script",
            "hibp-api-key": config["Api"]["key"],
        }

    def breachesAnAccount(self, account):
        apiUrl = "{}/breachedaccount/{}?truncateResponse=false".format(
            self.baseUrl1, account
        )
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            print("==================================================")
            print("[*] Warning; Breach Check for: {}".format(account))
            for data in resp.json():
                print("=========================")
                print("  - Name        : {}".format(data["Name"]))
                print("  - Title       : {}".format(data["Title"]))
                print("  - Domain      : {}".format(data["Domain"]))
                print("  - BreachDate  : {}".format(data["BreachDate"]))
                print("  - AddedDate   : {}".format(data["AddedDate"]))
                print("  - ModifiedDate: {}".format(data["ModifiedDate"]))
                print("  - PwnCount    : {}".format(data["PwnCount"]))
                print("  - Description :\n{}".format(data["Description"]))
                print("  - DataClasses : {}".format(", ".join(data["DataClasses"])))
                print("  - IsVerified  : {}".format(data["IsVerified"]))
                print("  - IsFabricated: {}".format(data["IsFabricated"]))
                print("  - IsSensitive : {}".format(data["IsSensitive"]))
                print("  - IsRetired   : {}".format(data["IsRetired"]))
                print("  - IsSpamList  : {}".format(data["IsSpamList"]))
                print("  - LogoPath    : {}".format(data["LogoPath"]))
        elif resp.status_code == 404:
            print("==================================================")
            print("[*] Info; {} not found in a breach".format(account))

    def allBreachedSites(self):
        apiUrl = "{}/breaches".format(self.baseUrl1)
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            for data in resp.json():
                print("=========================")
                print("  - Name        : {}".format(data["Name"]))
                print("  - Title       : {}".format(data["Title"]))
                print("  - Domain      : {}".format(data["Domain"]))
                print("  - BreachDate  : {}".format(data["BreachDate"]))
                print("  - AddedDate   : {}".format(data["AddedDate"]))
                print("  - ModifiedDate: {}".format(data["ModifiedDate"]))
                print("  - PwnCount    : {}".format(data["PwnCount"]))
                print("  - Description :\n{}".format(data["Description"]))
                print("  - DataClasses : {}".format(", ".join(data["DataClasses"])))
                print("  - IsVerified  : {}".format(data["IsVerified"]))
                print("  - IsFabricated: {}".format(data["IsFabricated"]))
                print("  - IsSensitive : {}".format(data["IsSensitive"]))
                print("  - IsRetired   : {}".format(data["IsRetired"]))
                print("  - IsSpamList  : {}".format(data["IsSpamList"]))
                print("  - LogoPath    : {}".format(data["LogoPath"]))

    def singleBreachedSites(self, name):
        apiUrl = "{}/breach/{}".format(self.baseUrl1, name,)
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            print("==================================================")
            print("  - Name        : {}".format(resp.json()["Name"]))
            print("  - Title       : {}".format(resp.json()["Title"]))
            print("  - Domain      : {}".format(resp.json()["Domain"]))
            print("  - BreachDate  : {}".format(resp.json()["BreachDate"]))
            print("  - AddedDate   : {}".format(resp.json()["AddedDate"]))
            print("  - ModifiedDate: {}".format(resp.json()["ModifiedDate"]))
            print("  - PwnCount    : {}".format(resp.json()["PwnCount"]))
            print("  - Description :\n{}".format(resp.json()["Description"]))
            print("  - DataClasses : {}".format(", ".join(resp.json()["DataClasses"])))
            print("  - IsVerified  : {}".format(resp.json()["IsVerified"]))
            print("  - IsFabricated: {}".format(resp.json()["IsFabricated"]))
            print("  - IsSensitive : {}".format(resp.json()["IsSensitive"]))
            print("  - IsRetired   : {}".format(resp.json()["IsRetired"]))
            print("  - IsSpamList  : {}".format(resp.json()["IsSpamList"]))
            print("  - LogoPath    : {}".format(resp.json()["LogoPath"]))
        elif resp.status_code == 404:
            print("==================================================")
            print("[*] Info; {} not found in a breach".format(name))

    def allDataClasses(self):
        apiUrl = "{}/dataclasses".format(self.baseUrl1)
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            for data in resp.json():
                print("  - {}".format(data))

    def pastesAnAccount(self, account):
        apiUrl = "{}/pasteaccount/{}".format(self.baseUrl1, account)
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            print("==================================================")
            print("[*] Warning; Breach Check for: {}".format(account))
            for data in resp.json():
                print("=========================")
                print("  - Source    : {}".format(data["Source"]))
                print("  - Id        : {}".format(data["Id"]))
                print("  - Title     : {}".format(data["Title"]))
                print("  - Date      : {}".format(data["Date"]))
                print("  - EmailCount: {}".format(data["EmailCount"]))
        elif resp.status_code == 404:
            print("==================================================")
            print("[*] Info; {} not found in a breach".format(account))

    def searchingByRange(self, password):
        hashchars = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        apiUrl = "{}/range/{}".format(self.baseUrl2, hashchars[:5])
        resp = requests.get(apiUrl, headers=self.headers)
        if resp.status_code == 200:
            print("==================================================")
            matchFlag = False
            for item in resp.text.splitlines():
                if item[0:35] == hashchars[5:]:
                    print("[*] Warning; {}; {}".format(password, item[36:]))
                    matchFlag = True
            if not matchFlag:
                print("[*] Info; {} not found in a breach".format(password))


if __name__ == "__main__":
    classhibp = HaveIBeenPwned()

    if args.breach is not None:
        classhibp.breachesAnAccount(args.breach)

    if args.allbreaches:
        classhibp.allBreachedSites()

    if args.site is not None:
        classhibp.singleBreachedSites(args.site)

    if args.dataclasses:
        classhibp.allDataClasses()

    if args.paste is not None:
        classhibp.pastesAnAccount(args.paste)

    if args.watchword is not None:
        classhibp.searchingByRange(args.watchword)
