#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from autotrader_custom_repo.AutoTrader.autotrader import options
from autotrader_custom_repo.AutoTrader.autotrader.brokers import trading

class Straddles_920:
    ''' 
    AutoTrader Strategy Template
    ----------------------------    
    '''

    def __init__(self, parameters, data, instrument):
        ''' Define all indicators used in the strategy '''
        self.name   = "920 Straddles"
        self.data   = data
        self.params = parameters
        
        # Get ATM strike
        atm_strike = options.getATMStrikePrice(self.data)
        logging.info(f"ATM Strike is {atm_strike}")

        #Set Instruments based on ATM Strike
        if (self.params['option_type'] == "both"):
            instrument_list = [{"strike": atm_strike, "option_type": "CE"}, {"strike": atm_strike, "option_type": "PE"}]
            self.symbol = trading.Symbol(instrument_list,self.params)

        self.trade_instrument = self.symbol.get_token()

        
    def generate_signal(self, data):
        ''' Define strategy to determine entry signals '''
        signal_dict = {}
        order_type  = 'market'
        #Short signal for instruments
        signal = -1
        stop = None
        take = None

        # Construct signal dictionary
        signal_dict["order_type"]   = order_type
        signal_dict["direction"]    = signal
        signal_dict["stop_loss"] = stop
        signal_dict["take_profit"] = take
        signal_dict["trade_instrument"] = self.trade_instrument
        return signal_dict
    