#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from autotrader_custom_repo.AutoTrader.autotrader import options
from autotrader_custom_repo.AutoTrader.autotrader.brokers.trading import Order, Symbol

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
        self.symbol = Symbol()


        
    def generate_signal(self, data):
        """Define strategy to determine entry signals."""
        orders = []

        # Get current position
        #for instrument in self.trade_instruments:
        current_position = self.broker.get_positions(self.trade_instruments)

        # Put entry strategy here
        if len(current_position) == 0:
            # Short trade instruments order:
            for instrument in self.trade_instruments:
                short_market_order = Order(direction=-1, order_type="market", instrument= instrument)
                orders.append(short_market_order)

        elif len(current_position) == len(self.trade_instruments):
            #We have all required  positions, now we just need to adjust them
            #Get LTP of positions
            for instrument in self.trade_instruments:
                row = data.get(instrument.get('token'))
                if row.right == "Call":
                    call_ltp = row.Close
                    call_instrument = instrument
                elif row.right == "Put":
                    put_ltp = row.Close
                    put_instrument = instrument


            if call_ltp <= put_ltp/2:
                modify_leg_order = Order(direction=1, order_type="market", instrument= call_instrument)
                new_trade_instruments = self.symbol.find_trade_instruments()
                orders.append(modify_leg_order)
            elif put_ltp <= call_ltp/2:
                modify_leg_order = Order(direction=1, order_type="market", instrument=put_instrument)
                new_trade_instruments = self.symbol.find_trade_instruments()
                orders.append(modify_leg_order)
        return orders
    