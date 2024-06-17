
from stocker_broker import StockerBrokerDriverInterface


class AutoTradingSystem:
    def __init__(self):
        self._driver = None

    def login(self, id, pw):
        self._driver.login(id, pw)

    def buy(self, stock_code, count, price):
        self._driver.buy(stock_code, count, price)

    def sell(self, stock_code, count, price):
        self._driver.sell(stock_code, count, price)


    @property
    def stock_broker_driver(self):
        return self._driver

    def select_stock_broker(self, driver: StockerBrokerDriverInterface):
        if not isinstance(driver, StockerBrokerDriverInterface):
            raise Exception
        self._driver = driver

