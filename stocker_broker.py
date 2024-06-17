from abc import ABC, abstractmethod


class StockerBrokerDriverInterface(ABC):
    pass


class KiwerDriver(StockerBrokerDriverInterface):
    def __init__(self, API):
        self.API = API


class NemoDriver(StockerBrokerDriverInterface):
    def __init__(self, API):
        self.API = API

    def login(self, id, pw):
        self.API.cerification(id, pw)

    def buy(self, stock_code, price, count):
        self.API.purchasing_stock(stock_code, price, count)

    def sell(self, stock_code, price, count):
        self.API.selling_stock(stock_code, price, count)