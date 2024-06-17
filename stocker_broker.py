from abc import ABC, abstractmethod

from kiwer_api import KiwerAPI
from nemo_api import NemoAPI


class StockerBrokerDriverInterface(ABC):
    pass


class KiwerDriver(StockerBrokerDriverInterface):
    def __init__(self, api: KiwerAPI):
        self.api = api


class NemoDriver(StockerBrokerDriverInterface):
    def __init__(self, api: NemoAPI):
        self.api = api
