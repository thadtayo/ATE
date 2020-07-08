
'''
Trade through Alpaca API.
'''
import requests
import json
from config import * 


# TODO: make different functions for each type of order
def create_order(symbol, quantity, side, type, time_in_force):
    data = {

    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

