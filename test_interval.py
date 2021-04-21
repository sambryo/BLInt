import unittest

from interval import Interval


class TestInterval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print(' teardownClass')

    def test_merge(self):
        self.interval_1 = Interval(1, 2)
        self.assertEqual(self.interval_1.merge("1-3"), "1-3")
        self.assertEqual(self.interval_1.merge("1-3,2,4,6-9"), "1-3,4,6-9")

    def test_pares_input(self):
        self.interval_1 = Interval(1, 2)
        self.assertEqual(self.interval_1.parse_input("1,2-3"), ["1", "2-3"])

        with self.assertRaises(ValueError):
            self.interval_1.parse_input("1-2-3")

    def test_find_indexes(self):
        self.interval_2 = Interval(3)
        self.assertEqual(self.interval_2.find_indexes(
            ["2"], ["3"]), [2, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
