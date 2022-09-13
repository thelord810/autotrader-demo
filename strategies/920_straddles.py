#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from autotrader_custom_repo.AutoTrader.autotrader import options

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
        self.trade_instrument = {"CE": atm_strike, "PE": atm_strike}

        
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
    