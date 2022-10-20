#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging


class Strangles:
    ''' 
    AutoTrader Strategy Template
    ----------------------------    
    '''

    def __init__(self, parameters, data, instrument, trade_instruments, broker, **kwargs):
        ''' Define all indicators used in the strategy '''
        self.name   = "Strangles"
        self.data   = data
        self.params = parameters
        self.instrument = instrument
        self.trade_instruments = trade_instruments
        self.broker = broker


        
    def generate_signal(self, data):
        """Define strategy to determine entry signals."""
        orders = []

        # Get current position
        current_position = self.broker.get_positions(self.trade_instruments)

        # Put entry strategy here
        signal = 0
        if len(current_position) == 0:
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
        signal_dict["trade_instrument"] = self.trade_instruments
        signal_dict["lot_size"] = self.trade_instruments[0].get('lot_size')
        return signal_dict
    