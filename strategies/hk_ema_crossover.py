# Import packages
from finta import TA
from autotrader_custom_repo.AutoTrader.autotrader.indicators import crossover
from autotrader_custom_repo.AutoTrader.autotrader.indicators import heikin_ashi
from autotrader_custom_repo.AutoTrader.autotrader.indicators import find_swings
from autotrader_custom_repo.AutoTrader.autotrader.brokers.trading import Order

class HKEMAcrossOver:
    '''
    EMA Crossover example strategy. 
    
    '''
    
    def __init__(self, parameters, data, instrument):
        ''' Define all indicators used in the strategy '''
        self.name   = "Strategy name"
        hk_data = heikin_ashi(data)
        self.data   = hk_data
        self.params = parameters
        self.instrument = instrument
        
        # EMA's
        self.ema = TA.EMA(hk_data, int(parameters['ema']))

        #Crossover condition of HK candle with EMA
        self.crossovers = crossover(self.data.Close,
                                    self.ema)
        # Price swings
        self.swings = find_swings(data)

        # Construct indicators dict for plotting
        self.indicators = {'EMA': {'type': 'MA',
                                        'data': self.ema}
                            }
        
    def generate_signal(self, i, current_position=""):
        ''' Define strategy to determine entry signals '''
        order_type      = 'market'
        related_orders  = None
        signal_dict     = {}
        # Put entry strategy here
        signal      = 0
        RR = self.params['RR']

        if (self.crossovers[i] == 1):
            # Long entry signal
            exit_dict = self.generate_exit_levels(signal=1, i=i)
            new_order = Order(direction=1,
                              stop_loss=exit_dict['stop_loss'],
                              take_profit=exit_dict['take_profit'])

        elif (self.data.Close[i - 1] == self.data.Low[i - 1]):
            new_order = Order(order_type='close')

        elif (self.crossovers[i] == -1):
            # Short entry signal
            exit_dict = self.generate_exit_levels(signal=-1, i=i)
            new_order = Order(direction=-1,
                              stop_loss=exit_dict['stop_loss'],
                              take_profit=exit_dict['take_profit'])

        elif (self.data.High[i - 1] == self.data.Open[i - 1]):
            new_order = Order(order_type='close')

        else:
            # No signal
            new_order = Order()

        return new_order

    def generate_exit_levels(self, signal, i):
        ''' Function to determine stop loss and take profit levels '''
        ...
        stop_type = 'market'
        RR = self.params['RR']

        stop = None
        take = None

        exit_dict = {'stop_loss': stop,
                     'stop_type': stop_type,
                     'take_profit': take}
        return exit_dict