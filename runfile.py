#from autotrader.autotrader import AutoTrader
from autotrader_custom_repo.AutoTrader.autotrader import  AutoTrader

at = AutoTrader()
keys_config = {
    "ICICI": {
        "appKey": "85450e08hYJ31324gc@727W093148d4E",
        "apiSecret": "02z38W87%9B36I8*8#776K72Q64597wB"
    }
}
# Create a new instance of AutoTrader
at.configure(show_plot=True, verbosity=1, broker= "kotak", feed='common', mode='continuous', allow_dancing_bears=True, global_config=keys_config, update_interval='1S', req_liveprice=True)#Configure the instance
# at.add_strategy('hk_ema_crossover')                     # Add the strategy by its configuration file prefix
# at.backtest(start = '1/10/2021',             # Define the backtest settings
#             end = '23/12/2021',
#             initial_balance=100000,
#             leverage = 30)

# at.configure(show_plot=True, verbosity=1)   # Configure the instance
at.add_strategy('920_straddles')                     # Add the strategy by its configuration file prefix
#at.backtest(start = '1/1/2021',             # Define the backtest settings
#            end = '1/1/2022')
at.run()
