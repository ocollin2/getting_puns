# download and print puns from an API

import requests
import json

# download a random pun from https://www.punapi.rest/
pun_url_request = requests.get("https://www.punapi.rest/api/pun")
pun_data = json.loads(pun_url_request.content)

print(pun_data)