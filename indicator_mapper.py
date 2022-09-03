'''
AutoTrader Indiview
--------------------
A general script to view price data and indicators.
'''

from autotrader.autodata import GetData
from autotrader.autoplot import AutoPlot
from autotrader import indicators

# Instantiate GetData class
broker_config = {'data_source': 'ICICI', 'appKey': '85450e08hYJ31324gc@727W093148d4E', 'apiSecret': '02z38W87%9B36I8*8#776K72Q64597wB'}
get_data = GetData(broker_config)

# Get price data for EUR/USD
instrument = 'NIFTY'
extra_attributes = {"exchange": "NFO",
                    "product": "futures",
                    "expiry": "2021-12-30T07:00:00.000Z",
                    "option_type": "",
                    "strike": "",
                    "start_date": "2021-10-01T07:00:00.000Z",
                    "end_date": "2021-12-23T07:00:00.000Z"
                    }
data = get_data.icici(instrument,"1minute",count=1,**extra_attributes)
hk_data = indicators.heikin_ashi(data)

# Construct indicators dictionary
supertrend_df = indicators.supertrend(hk_data)
indicator_dict = {'SuperTrend': {'type': 'Supertrend',
                                'data': supertrend_df}}

# Instantiate AutoPlot and plot
ap = AutoPlot(data)
ap.plot(indicators=indicator_dict, instrument=instrument)