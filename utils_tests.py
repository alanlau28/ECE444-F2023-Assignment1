from utils import Utils
import unittest

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(Utils.reversed(1234),4321)
        self.assertEqual(Utils.reversed('1234'),4321)
        self.assertEqual(Utils.reversed(1234.123),4321)

    def test_formatter(self):
        self.assertEqual(Utils.formatter(1234),('0b10011010010','0o2322'))
        self.assertEqual(Utils.formatter('1234'),('0b10011010010','0o2322'))
        self.assertEqual(Utils.formatter(1234.123),('0b10011010010','0o2322'))

if __name__ == '__main__':
    unittest.main()