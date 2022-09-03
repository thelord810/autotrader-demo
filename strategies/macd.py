from finta import TA
import autotrader.indicators as indicators
from autotrader.brokers.trading import Order


class SimpleMACD:
    """Simple MACD Strategy

    Rules
    ------
    1. Trade in direction of trend, as per 200EMA.
    2. Entry signal on MACD cross below/above zero line.
    3. Set stop loss at recent price swing.
    4. Target 1.5 take profit.
    """
<<<<<<< Updated upstream
    
=======

>>>>>>> Stashed changes
    def __init__(self, parameters, data, instrument):
        """Define all indicators used in the strategy.
        """
        self.name = "MACD Trend Strategy"
        self.data = data
        self.params = parameters
        self.instrument = instrument

        # 200EMA
        self.ema = TA.EMA(data, parameters['ema_period'])
<<<<<<< Updated upstream
        
=======

>>>>>>> Stashed changes
        # MACD
        self.MACD = TA.MACD(data, self.params['MACD_fast'],
                            self.params['MACD_slow'], self.params['MACD_smoothing'])
        self.MACD_CO = indicators.crossover(self.MACD.MACD, self.MACD.SIGNAL)
        self.MACD_CO_vals = indicators.cross_values(self.MACD.MACD,
                                                    self.MACD.SIGNAL,
                                                    self.MACD_CO)

        # Price swings
        self.swings = indicators.find_swings(data)

        # Construct indicators dict for plotting
        self.indicators = {'MACD (12/26/9)': {'type': 'MACD',
                                              'macd': self.MACD.MACD,
                                              'signal': self.MACD.SIGNAL,
<<<<<<< Updated upstream
                                              'histogram': self.MACD.MACD-self.MACD.SIGNAL},
=======
                                              'histogram': self.MACD.MACD - self.MACD.SIGNAL},
>>>>>>> Stashed changes
                           'EMA (200)': {'type': 'MA',
                                         'data': self.ema}}

    def generate_signal(self, i, current_position="",**kwargs):
        """Define strategy to determine entry signals.
        """

        if self.data.Close.values[i] > self.ema[i] and \
                self.MACD_CO[i] == 1 and \
                self.MACD_CO_vals[i] < 0:
            exit_dict = self.generate_exit_levels(signal=1, i=i)
            new_order = Order(direction=1,
                              stop_loss=exit_dict['stop_loss'],
                              take_profit=exit_dict['take_profit'])

        elif self.data.Close.values[i] < self.ema[i] and \
                self.MACD_CO[i] == -1 and \
                self.MACD_CO_vals[i] > 0:
            exit_dict = self.generate_exit_levels(signal=-1, i=i)
            new_order = Order(direction=-1,
                              stop_loss=exit_dict['stop_loss'],
                              take_profit=exit_dict['take_profit'])

        else:
            new_order = Order()

        return new_order

    def generate_exit_levels(self, signal, i):
        """Function to determine stop loss and take profit levels.
        """
        stop_type = 'limit'
        RR = self.params['RR']

        if signal == 0:
            stop = None
            take = None
        else:
            if signal == 1:
                stop = self.swings.Lows[i]
                take = self.data.Close[i] + RR * (self.data.Close[i] - stop)
            else:
                stop = self.swings.Highs[i]
                take = self.data.Close[i] - RR * (stop - self.data.Close[i])

        exit_dict = {'stop_loss': stop,
                     'stop_type': stop_type,
                     'take_profit': take}

        return exit_dict