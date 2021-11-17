from unittest.mock import patch
from unittest import *
from Lottery import *


class TestLottery(TestCase):
    def setUp(self):
        self.lottery=Lottery()
        print("set up")
    def tearDown(self):
        print(self.lottery.numbers)
        print("tear down")

    def test_rand_numbers(self):
        self.assertEqual(len(self.lottery.rand_numbers()),6)

    def test_valid_numbers(self):
        ex=self.lottery
        res = ex.valid_numbers()
        self.assertTrue(res)
    @mock.patch
    def test_valid_range(self):
        bool=self.lottery.valid_range()
        print(self.lottery.numbers)
        self.assertTrue(bool)
