

class AutoTradingSystem:
    def __init__(self):
        self.stock_broker_driver = None
    def select_stock_broker(self, kiwer_driver):
        self.stock_broker_driver = kiwer_driver

    def login(self, id, pw):
        self.stock_broker_driver.login(id, pw)

    def buy(self, stock_code, count, price):
        self.stock_broker_driver.buy(stock_code, count, price)

    def sell(self, stock_code, count, price):
        self.stock_broker_driver.sell(stock_code, count, price)
