# Import packages
from finta import TA
from autotrader.indicators import crossover
from autotrader.indicators import heikin_ashi

class HKSMAcrossOver:
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
        self.sma = TA.SMA(hk_data, int(parameters['sma']))

        #self.crossovers = crossover(self.ema,
        #                           self.data)
        
        # Construct indicators dict for plotting
        self.indicators = {'SMA': {'type': 'MA',
                                        'data': self.sma}
                            }
        
    def generate_signal(self, i, current_position=""):
        ''' Define strategy to determine entry signals '''
        order_type      = 'market'
        related_orders  = None
        signal_dict     = {}
        # Put entry strategy here
        signal      = 0
        RR = self.params['RR']

        #Crossover condition of HK candle with SMA
        if self.data.Close[i] > self.sma[i]:
            # Long entry signal
            signal = 1
            stop = self.data.Low[i] < self.data.Low[i-1]
            take = self.data.Close[i] + RR * (self.data.Close[i] - stop)

        elif self.data.Close[i] < self.sma[i]:
            # Short entry signal
            signal = -1
            stop = self.data.High[i] > self.data.High[i-1]
            take = self.data.Close[i] + RR * (self.data.Close[i] - stop)

        else:
            # No signal
            signal = 0
            stop = None
            take = None
        
        # Construct signal dictionary
        signal_dict["order_type"]   = order_type
        signal_dict["direction"]    = signal
        signal_dict["related_orders"] = related_orders
        
        return signal_dict

