import json
import re
try:

    with open(".\\.lip\\metadata\\github.com%2FLiteLDev%2Fbds.json") as file:
        json_data = file.read()
except FileNotFoundError:
    print("File not found")
    raise SystemExit
except Exception as e:
    print(e)
    raise SystemExit
data = json.loads(json_data)

post_install_command = data['commands']['post_install'][0]
match = re.search(r'version://windows/([^\\]+)', post_install_command)

if match:
    version_number = match.group(1)
    print(version_number)
else:
    print("???")
    