import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from domain.entity import NumberItemEntity

class TestFibonacciSeriesEntity(unittest.TestCase):
    def testNumber1ItemsEntity(self):
        self.assertEqual(NumberItemEntity(1).toJson()['number_item'], 1)

    def testNumber10ItemsEntity(self):
        self.assertEqual(NumberItemEntity(10).toJson()['number_item'], 10)

    def testNumberMinus1ItemsEntity(self):
        self.assertEqual(NumberItemEntity(-1).toJson()['number_item'], -1)

    def testStringItemsEntity(self):
        self.assertEqual(NumberItemEntity('1').toJson()['number_item'], '1')

    def testFloatItemsEntity(self):
        self.assertEqual(NumberItemEntity(1.0).toJson()['number_item'], 1.0)

    def testListItemsEntity(self):
        self.assertEqual(NumberItemEntity([1, 2, 3]).toJson()['number_item'], [1, 2, 3])

    def testTupleItemsEntity(self):
        self.assertEqual(NumberItemEntity((1, 2, 3)).toJson()['number_item'], (1, 2, 3))

    def testDictItemsEntity(self):
        self.assertEqual(NumberItemEntity({"a": 1}).toJson()['number_item'], {"a": 1})

    def testSetItemsEntity(self):
        self.assertEqual(NumberItemEntity({1, 2, 3}).toJson()['number_item'], {1, 2, 3})

if __name__ == "__main__":
    unittest.main()