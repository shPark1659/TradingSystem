import unittest
from unittest.mock import Mock

from auto_trading_system import AutoTradingSystem
from kiwer_api import KiwerAPI
from nemo_api import NemoAPI
from stocker_broker import StockerBrokerDriverInterface, KiwerDriver, NemoDriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.auto_trading = AutoTradingSystem()

        self.mk_kiwer_api = Mock(spec=KiwerAPI)
        self.mk_kiwer_api.login.side_effect = lambda id, pw: print(id + ' login success')
        self.mk_kiwer_api.buy.side_effect = lambda stock_code, count, price: print(stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))
        self.mk_kiwer_api.sell.side_effect = lambda stock_code, count, price: print(stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(count))
        self.mk_nemo_api = Mock(spec=NemoAPI)
        self.mk_nemo_api.cerification.side_effect = lambda id, pw:  print('[NEMO]' + id + ' login GOOD')
        self.mk_nemo_api.purchasing_stock.side_effect = lambda stock_code, price, count: print('[NEMO]' + stock_code + ' buy stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')
        self.mk_nemo_api.selling_stock.side_effect = lambda stock_code,  price, count: print('[NEMO]' + stock_code + ' sell stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')

        self.kiwer_driver = KiwerDriver(api=self.mk_kiwer_api)
        self.nemo_driver = KiwerDriver(api=self.mk_nemo_api)

    def test_success_select_stock_broker(self):
        drivers = {'키워': self.kiwer_driver, '네모': self.nemo_driver}

        for key, values in drivers.items():
            with self.subTest('sub_test_' + key):
                self.auto_trading.select_stock_broker(values)
                if key == '키워':
                    self.assertIsTrue(isinstance(self.auto_trading.stock_broker_driver, KiwerDriver))
                elif key == '네모':
                    self.assertIsTrue(isinstance(self.auto_trading.stock_broker_driver, NemoDriver))

    def test_fail_select_stock_broker(self):
        with self.assertRaises(Exception):
            self.select_stock_broker('Noname')

    def test_buy_sell_with_kiwer(self):
        self.auto_trading.select_stock_broker(self.kiwer_driver)

        self.auto_trading.login('ID', 'PW')
        self.auto_trading.buy('ABC', 100, 5)
        self.auto_trading.sell('ABC', 110, 5)

        self.assertEqual(1, self.mk_kiwer_api.login.call_count)
        self.assertEqual(1, self.mk_kiwer_api.buy.call_count)
        self.assertEqual(1, self.mk_kiwer_api.sell.call_count)

    def test_buy_sell_with_nemo(self):
        self.auto_trading.select_stock_broker(self.nemo_driver)

        self.auto_trading.login('ID', 'PW')
        self.auto_trading.buy('ABC', 100, 5)
        self.auto_trading.sell('ABC', 110, 5)

        self.assertEqual(1, self.mk_nemo_api.cerification.call_count())
        self.assertEqual(1, self.mk_nemo_api.purchasing_stock.call_count())
        self.assertEqual(1, self.mk_nemo_api.selling_stock.call_count())


if __name__ == '__main__':
    unittest.main()
