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

    def buy_nice_timing(self, stock_code, cash_amount):
        if self.is_bullish(stock_code):
            current_price = self.get_price(stock_code)
            max_amount = int(cash_amount / current_price)
            self.buy(stock_code, max_amount, current_price)

    def sell_nice_timing(self, stock_code, stock_amount):
        if self.is_bearish(stock_code):
            current_price = self.get_price(stock_code)
            self.sell(stock_code, stock_amount, current_price)

    def is_bullish(self, stock_code):
        tick_1 = self.get_price(stock_code)
        tick_2 = self.get_price(stock_code)
        tick_3 = self.get_price(stock_code)
        if tick_1 < tick_2 and tick_2 < tick_3:
            return True
        return False

    def is_bearish(self, stock_code):
        tick_1 = self.get_price(stock_code)
        tick_2 = self.get_price(stock_code)
        tick_3 = self.get_price(stock_code)
        if tick_1 > tick_2 and tick_2 > tick_3:
            return True
        return False

    @property
    def stock_broker_driver(self):
        return self._driver

    def select_stock_broker(self, driver: StockerBrokerDriverInterface):
        if not isinstance(driver, StockerBrokerDriverInterface):
            raise Exception
        self._driver = driver

    def get_price(self, stock_code):
        return self._driver.current_price(stock_code)
