class AutoTradingSystem:
    def select_stock_broker(self, driver):
        self.broker = driver

    def login(self, param, param1):
        self.broker.login(param, param1)

    def buy(self, param, param1, param2):
        self.broker.buy(param, param1, param2)

    def sell(self, param, param1, param2):
        self.broker.sell(param, param1, param2)