'''
Fetches all historical data.
'''
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import config

# remove on deployment
import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)

ts = TimeSeries(config.ALPHA_VANTAGE_KEY)

'''
Gets n [ default = 100 ] daily
open, high, low, close, volume.
If entries m < n, it returns m entries instead.
If n='full', run full
'''
def get_daily(symbol, n=100):
    # run full mode
    stock = {}
    meta = {}
    if n == 'full' or n > 100:
        stock, meta = ts.get_daily(symbol=symbol, outputsize='full')

    # run compact mode
    else:
        stock, meta = ts.get_daily(symbol=symbol, outputsize='compact')

    return stock, meta
    



if __name__ == '__main__':
    get_daily(sys.argv[1], sys.argv[2])

    