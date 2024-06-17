import unittest
from unittest.mock import Mock

from auto_trading_system import AutoTradingSystem
from kiwer_api import KiwerAPI
from stocker_broker import StockerBrokerDriverInterface, KiwerDriver, NemoDriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.auto_trading = AutoTradingSystem()

    def test_success_select_stock_broker(self):
        drivers = {'키워': KiwerDriver, '네모': NemoDriver}

        for key, values in drivers.items():
            with self.subTest('sub_test_' + key):
                self.auto_trading.select_stock_broker(key)
                self.assertIsTrue(isinstance(self.auto_trading.stock_broker_driver, values))

    def test_fail_select_stock_broker(self):
        with self.assertRaises(Exception):
            self.select_stock_broker('Noname')

    def test_buy_sell_with_nemo(self):
        self.auto_trading.select_stock_broker('네모')
        mk_nemo_api = Mock(spec=KiwerAPI)
        mk_nemo_api.login.return_value = True
        mk_nemo_api.buy.return_value = True
        mk_nemo_api.sell.return_value = True

        self.auto_trading.login('ID', 'PW')
        self.auto_trading.buy('ABC', 100, 5)
        self.auto_trading.sell('ABC', 110, 5)

        self.assertEqual(1, mk_nemo_api.login.call_count())
        self.assertEqual(1, mk_nemo_api.buy.call_count())
        self.assertEqual(1, mk_nemo_api.sell.call_count())


if __name__ == '__main__':
    unittest.main()
