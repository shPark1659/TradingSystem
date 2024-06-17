from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI


class StockerBrokerDriverInterface(ABC):
    def __init__(self, API):
        self.api = API

    @abstractmethod
    def login(self, id, password):
        raise NotImplementedError("need to implement")

    @abstractmethod
    def current_price(self, stock_code):
        raise NotImplementedError("need to implement")


class KiwerDriver(StockerBrokerDriverInterface):
    def login(self, id, password):
        self.api.login(id, password)

    def current_price(self, stock_code):
        return self.api.current_price(stock_code)


class NemoDriver(StockerBrokerDriverInterface):
    def login(self, id, password):
        pass

    def current_price(self, stock_code):
        pass
