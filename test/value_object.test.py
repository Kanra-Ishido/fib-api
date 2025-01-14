import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from domain.value_object.items import FibonacciSeriesValueObject

class TestFibonacciSeriesValueObject(unittest.TestCase):
    def testInteger1ValueObject(self):
        self.assertEqual(FibonacciSeriesValueObject(1).execute_input(), 1)

    def testInteger10ValueObject(self):
        self.assertEqual(FibonacciSeriesValueObject(10).execute_input(), 10)

    def testInteger100ValueObject(self):
        self.assertEqual(FibonacciSeriesValueObject(100).execute_input(), 100)

    def testMinusValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject(-1).execute_input()
        self.assertEqual(str(context.exception), "負の値が入力されています、正の整数を入力してください")

    def testFloatValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject(1.1).execute_input()
        self.assertEqual(str(context.exception), "小数が入力されています、正の整数を入力してください")
        
    def testStringValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject("test").execute_input()
        self.assertEqual(str(context.exception), "文字列が入力されています、正の整数を入力してください")

    def testExistValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject().execute_input()
        self.assertEqual(str(context.exception), "値が存在しません、正の整数を入力してください")

    def testSingleListValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject([1, 2, 3]).execute_input()
        self.assertEqual(str(context.exception), "値が複数あります、単一の正の整数を入力してください")
    
    def testSingleTupleValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject((1, 2, 3)).execute_input()
        self.assertEqual(str(context.exception), "値が複数あります、単一の正の整数を入力してください")

    def testSingleDictValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject({"a": 1}).execute_input()
        self.assertEqual(str(context.exception), "値が複数あります、単一の正の整数を入力してください")

    def testSingleSetValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesValueObject({1, 2, 3}).execute_input()
        self.assertEqual(str(context.exception), "値が複数あります、単一の正の整数を入力してください")

if __name__ == "__main__":
    unittest.main()