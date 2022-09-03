<<<<<<< Updated upstream
from autotrader import AutoTrader

# Create AutoTrader instance, configure it, and run backtest
at = AutoTrader()
at.configure(verbosity=1, show_plot=True, feed='yahoo', mode='periodic')
at.add_strategy('macd')
at.backtest(start = '1/1/2022', end = '1/5/2022')
at.virtual_account_config(initial_balance=1000, leverage = 30)
at.run()

=======
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
at.configure(show_plot=True, verbosity=1, broker="kotak", feed='common', mode="continuous", allow_dancing_bears=True, global_config=keys_config)#Configure the instance
# at.add_strategy('hk_ema_crossover')                     # Add the strategy by its configuration file prefix
# at.backtest(start = '1/10/2021',             # Define the backtest settings
#             end = '23/12/2021',
#             initial_balance=100000,
#             leverage = 30)

# at.configure(show_plot=True, verbosity=1)   # Configure the instance
at.add_strategy('sma_momentum')                     # Add the strategy by its configuration file prefix
at.backtest(start = '1/1/2021',             # Define the backtest settings
            end = '1/1/2022')
at.run()  
>>>>>>> Stashed changes
