import requests
from pprint import pprint
endpoint = 'http://127.0.0.1:8000/car/list'

getresponse = requests.get(endpoint)

# pprint(getresponse.json())
pprint(getresponse.status_code)