from stocker_broker import StockerBrokerDriverInterface


class AutoTradingSystem:
    def select_stock_broker(self, stock_broker: StockerBrokerDriverInterface):
        self.__driver = stock_broker

    def login(self, id, password):
        return self.__driver.login(id, password)

    def current_price(self, stock_code):
        return self.__driver.current_price(stock_code)
