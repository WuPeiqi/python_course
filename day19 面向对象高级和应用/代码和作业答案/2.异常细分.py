import requests
from requests.exceptions import InvalidSchema, MissingSchema

try:
    res = requests.get(url="asdfasdf")
except InvalidSchema as e:
    print("InvalidSchema", e)
except MissingSchema as e:
    print("MissingSchema", e)
except Exception as e:
    print("Exception", e)
