from abc import ABC, abstractmethod


class StockerBrokerDriverInterface(ABC):
    pass


class KiwerDriver(StockerBrokerDriverInterface):
    pass


class NemoDriver(StockerBrokerDriverInterface):
    pass
