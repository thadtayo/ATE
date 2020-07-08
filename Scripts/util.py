import requests
import json
from config import * 

'''
Logs trades.
'''
def log(statement):
    print('...')

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)
