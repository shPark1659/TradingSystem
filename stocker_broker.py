from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class StockerBrokerDriverInterface(ABC):
    def __init__(self, api):
        self.api = api

    @abstractmethod
    def login(self, id, password):
        raise NotImplementedError("need to implement")

    @abstractmethod
    def buy(self, stock_code, count, price):
        pass

    @abstractmethod
    def sell(self, stock_code, count, price):
        pass

    @abstractmethod
    def current_price(self, stock_code):
        raise NotImplementedError("need to implement")


class KiwerDriver(StockerBrokerDriverInterface):
    def login(self, id, password):
        self.api.login(id, password)

    def buy(self, stock_code, count, price):
        self.api.buy(stock_code, count, price)

    def sell(self, stock_code, count, price):
        self.api.sell(stock_code, count, price)

    def current_price(self, stock_code):
        return self.api.current_price(stock_code)


class NemoDriver(StockerBrokerDriverInterface):
    def login(self, id, password):
        self.api.cerification(id, password)

    def current_price(self, stock_code):
        return self.api.get_market_price(stock_code)

    def buy(self, stock_code, price, count):
        self.api.purchasing_stock(stock_code, price, count)

    def sell(self, stock_code, price, count):
        self.api.selling_stock(stock_code, price, count)