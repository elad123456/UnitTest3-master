from unittest import TestCase, mock
from unittest.mock import patch
from package1.Lottery import *


class TestLottery(TestCase):
    def setUp(self):
        self.lottery=Lottery()
        print("set up")

    def tearDown(self):
        print("tear down")

    def test_rand_numbers(self):
        self.assertEqual(len(self.lottery.rand_numbers()),6)

    def test_valid_numbers(self):
        with patch('package1.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [0, 1, 2, 3, 0, 5]
            print(mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_numbers())


    def test_valid_range(self):
        with patch('package1.Lottery.Lottery.rand_numbers') as mock_rand_num:
            mock_rand_num.return_value = [0, 0, 0, 0, 0, -100]
            print(mock_rand_num.return_value)
            self.assertFalse(self.lottery.valid_range())
            mock_rand_num.return_value=[22,6,2,3,4,5]
            print(mock_rand_num.return_value)
            self.assertTrue(self.lottery.valid_range())
