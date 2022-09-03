from autotrader.autotrader import AutoTrader

at = AutoTrader()                           # Create a new instance of AutoTrader
at.configure(show_plot=True, verbosity=1, broker="ib", feed='icici')   # Configure the instance
at.add_strategy('hk_sma_crossover')                     # Add the strategy by its configuration file prefix

at.run()  