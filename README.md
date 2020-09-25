# HaveIBeenPwned
Have I Been Pwned API(v3)

To execute this script, the following modules are required.
- configparser
- Hashlib
- argparse
- requests

Please install the requests module separately by the following command<br>
"pip install requests"

# Usage
./HaveIBeenPwned.py [-h] [-b BREACH] [-a] [-s SITE] [-d] [-p PASTE] [-w WATCHWORD]

optional arguments:<br>
-h, --help show this help message and exit.<br>
-b BREACH, --breach BREACH{MailAddress} Getting all breaches for an account.<br>
-a, --allbreaches Getting all breached sites in the system.<br>
-s SITE, --site SITE{Name} Getting a single breached site.<br>
-d, --dataclasses Getting all data classes in the system.<br>
-p PASTE, --paste PASTE{MailAddress} Getting all pastes for an account.<br>
-w WATCHWORD, --watchword WATCHWORD{Password} Searching by range.<br>

# Reference Information
https://haveibeenpwned.com<br>
https://haveibeenpwned.com/API/v3<br>
https://haveibeenpwned.com/API/Key<br>
