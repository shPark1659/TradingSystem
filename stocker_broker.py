from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI


class StockerBrokerDriverInterface(ABC):
    @abstractmethod
    def login(self, id, password):
        pass

    @abstractmethod
    def buy(self, stock_code, count, price):
        pass

    @abstractmethod
    def sell(self, stock_code, count, price):
        pass


class KiwerDriver(StockerBrokerDriverInterface):
    def __init__(self, API):
        super().__init__()
        self._kiwer_api = API

    def login(self, id, password):
        self._kiwer_api.login(id, password)

    def buy(self, stock_code, count, price):
        self._kiwer_api.buy(stock_code, count, price)

    def sell(self, stock_code, count, price):
        self._kiwer_api.sell(stock_code, count, price)

class NemoDriver(StockerBrokerDriverInterface):
    pass
