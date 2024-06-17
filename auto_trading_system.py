from stocker_broker import StockerBrokerDriverInterface


class AutoTradingSystem:
    def __init__(self):
        self._driver = None

    @property
    def stock_broker_driver(self):
        return self._driver

    def select_stock_broker(self, driver: StockerBrokerDriverInterface):
        if not isinstance(driver, StockerBrokerDriverInterface):
            raise Exception
        self._driver = driver
