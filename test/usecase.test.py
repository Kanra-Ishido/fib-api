import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from application.usecase import FibonacciSeriesUsecase

class TestFibonacciSeriesUsecase(unittest.TestCase):
    def testInteger1Usecase(self):
        self.assertEqual(FibonacciSeriesUsecase(1).execute(), 1)

    def testInteger10Usecase(self):
        self.assertEqual(FibonacciSeriesUsecase(10).execute(), 55)

    def testInteger100Usecase(self):
        self.assertEqual(FibonacciSeriesUsecase(100).execute(), 354224848179261915075)

    def testMinusUsecase(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase(-1).execute()
        self.assertEqual(str(context.exception), '負の値が入力されています、正の整数を入力してください')

    def testFloatUsecase(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase(1.1).execute()
        self.assertEqual(str(context.exception), '小数が入力されています、正の整数を入力してください')

    def testStringValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase('test').execute()
        self.assertEqual(str(context.exception), '文字列が入力されています、正の整数を入力してください')

    def testExistValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase().execute()
        self.assertEqual(str(context.exception), '値が存在しません、正の整数を入力してください')

    def testSingleListValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase([1, 2, 3]).execute()
        self.assertEqual(str(context.exception), '値が複数あります、単一の正の整数を入力してください')

    def testSingleTupleValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase((1, 2, 3)).execute()
        self.assertEqual(str(context.exception), '値が複数あります、単一の正の整数を入力してください')

    def testSingleDictValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase({'a': 1}).execute()
        self.assertEqual(str(context.exception), '値が複数あります、単一の正の整数を入力してください')

    def testSingleSetValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase({1, 2, 3}).execute()
        self.assertEqual(str(context.exception), '値が複数あります、単一の正の整数を入力してください')

    def testInteger99999ValueObject(self):
        with self.assertRaises(ValueError) as context:
            FibonacciSeriesUsecase(99999).execute()
        self.assertEqual(str(context.exception), '4096桁を超える値の出力はできません、4096桁以下の出力になる正の整数を入力してください')

if __name__ == '__main__':
    unittest.main()