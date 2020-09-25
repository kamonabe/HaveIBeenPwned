# HaveIBeenPwned
Have I Been Pwned API(v3)

To execute this script, the following modules are required.
- configparser
- Hashlib
- argparse
- The requirements

Please install the requests module separately by the following command
"pip install requests"

# Usage
./HaveIBeenPwned.py [-h] [-b BREACH] [-p PASTE] [-w WATCHWORD]

optional arguments:<br>
-h, --help show this help message and exit.<br>
-b BREACH, --breach BREACH{MailAddress} Getting all breaches for an account.<br>
-p PASTE, --paste PASTE{MailAddress} Getting all pastes for an account.<br>
-w WATCHWORD, --watchword WATCHWORD{Password} Searching by range.<br>
