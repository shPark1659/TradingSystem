import unittest
from unittest.mock import Mock
import random

from auto_trading_system import AutoTradingSystem
from kiwer_api import KiwerAPI
from nemo_api import NemoAPI
from stocker_broker import StockerBrokerDriverInterface, KiwerDriver, NemoDriver

TEST_ID = "my_id"
TEST_PW = "my_pw"
STOCK_COUNT = 5
STOCK_CODE = 'SEC'
AVG_STOCK_PRICE = 5450
STR_KIWER = 'kiwer'
STR_NEMO = 'nemo'
DRIVERS = [STR_KIWER, STR_NEMO]
PRICE_TABLE = [
    list(range(5000, 5901, 36)) + list(range(5900 - 36, 5000, -36)) + list(range(5000 + 36, 5901, 36)),
    list(range(5000, 5451, 18)) + [5450]*23 + list(range(5450, 5901, 18)),
    list(range(5900, 5450, -18)) + [5450]*25 + list(range(5450, 5000, -18))
]
EXPECTED_TABLE = tuple(tuple(row) for row in PRICE_TABLE)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        random.seed(10)

        self.mk_kiwer_api = Mock(spec=KiwerAPI)
        self.mk_kiwer_api.login.side_effect = lambda id, pw: print(id + ' login success')
        self.mk_kiwer_api.buy.side_effect = lambda stock_code, count, price: print(
            stock_code + ' : Buy stock ( ' + str(price) + ' * ' + str(count))
        self.mk_kiwer_api.sell.side_effect = lambda stock_code, count, price: print(
            stock_code + ' : Sell stock ( ' + str(price) + ' * ' + str(count))

        self.mk_nemo_api = Mock(spec=NemoAPI)
        self.mk_nemo_api.cerification.side_effect = lambda id, pw: print('[NEMO]' + id + ' login GOOD')
        self.mk_nemo_api.purchasing_stock.side_effect = lambda stock_code, price, count: print(
            '[NEMO]' + stock_code + ' buy stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')
        self.mk_nemo_api.selling_stock.side_effect = lambda stock_code, price, count: print(
            '[NEMO]' + stock_code + ' sell stock ( price : ' + str(price) + ' ) * ( count : ' + str(count) + ')')

        self.drivers = {STR_KIWER: KiwerDriver(api=self.mk_kiwer_api), STR_NEMO: NemoDriver(api=self.mk_nemo_api),}
        self.auto_trading = AutoTradingSystem()
        a = []
        for _ in range(10):
            a.append(self.mk_kiwer_api.current_price(100))
            a.append(self.mk_nemo_api.get_market_price(100))
        pass

    def test_success_select_stock_broker(self):
        for key, values in self.drivers.items():
            with self.subTest('sub_test_' + key):
                self.auto_trading.select_stock_broker(values)
                
                if key == STR_KIWER:
                    self.assertTrue(isinstance(self.auto_trading.stock_broker_driver, KiwerDriver))
                elif key == STR_NEMO:
                    self.assertTrue(isinstance(self.auto_trading.stock_broker_driver, NemoDriver))

    def test_fail_select_stock_broker(self):
        with self.assertRaises(Exception):
            self.auto_trading.select_stock_broker('Noname')

    def test_buy_sell_with_kiwer(self):
        self.auto_trading.select_stock_broker(self.drivers[STR_KIWER])

        self.auto_trading.login(TEST_ID, TEST_PW)
        self.auto_trading.buy(STOCK_CODE, STOCK_COUNT, AVG_STOCK_PRICE)
        self.auto_trading.sell(STOCK_CODE, STOCK_COUNT, AVG_STOCK_PRICE)

        self.assertEqual(1, self.mk_kiwer_api.login.call_count)
        self.assertEqual(1, self.mk_kiwer_api.buy.call_count)
        self.assertEqual(1, self.mk_kiwer_api.sell.call_count)

    def test_buy_sell_with_nemo(self):
        self.auto_trading.select_stock_broker(self.drivers[STR_NEMO])

        self.auto_trading.login(TEST_ID, TEST_PW)
        self.auto_trading.buy(STOCK_CODE, AVG_STOCK_PRICE, STOCK_COUNT)
        self.auto_trading.sell(STOCK_CODE, AVG_STOCK_PRICE, STOCK_COUNT)

        self.assertEqual(1, self.mk_nemo_api.cerification.call_count())
        self.assertEqual(1, self.mk_nemo_api.purchasing_stock.call_count())
        self.assertEqual(1, self.mk_nemo_api.selling_stock.call_count())

    def test_get_price_with_kiwer(self):
        self.auto_trading.select_stock_broker(self.drivers[STR_KIWER])
        self.auto_trading.login(TEST_ID, TEST_PW)
        self.mk_kiwer_api.current_price.side_effect = lambda x: PRICE_TABLE[0].pop(0)

        for idx in range(10):
            with self.subTest('sub_test_' + str(idx)):
                self.assertEqual(EXPECTED_TABLE[0][idx], self.auto_trading.get_price(STOCK_CODE))
        self.assertEqual(1, self.mk_kiwer_api.login.call_count())
        self.assertEqual(10, self.mk_kiwer_api.current_price.call_count())

    def test_get_price_with_nemo(self):
        self.auto_trading.select_stock_broker(self.drivers[STR_NEMO])
        self.auto_trading.cerification(TEST_ID, TEST_PW)
        self.mk_nemo_api.get_market_price.side_effect = lambda x, y: PRICE_TABLE[0].pop(0)

        for idx in range(10):
            with self.subTest('sub_test_' + str(idx)):
                self.assertEqual(EXPECTED_TABLE[0][idx], self.auto_trading.get_price(STOCK_CODE))
        self.assertEqual(1, self.mk_nemo_api.cerification.call_count())
        self.assertEqual(10, self.mk_nemo_api.get_market_price.call_count())


if __name__ == '__main__':
    unittest.main()
