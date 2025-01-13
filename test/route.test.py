import os
import sys
import unittest
from fastapi.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from main import app

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = TestClient(app)

    def testInteger1ValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result":1})

    def testInteger10ValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=10")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result":55})

    def testInteger100ValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=100")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result":354224848179261915075})

    def testMinusValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=-1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"負の値が入力されています、正の整数を入力してください"})

    def testFloatValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"小数が入力されています、正の整数を入力してください"})

    def testStringValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=test")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"文字列が入力されています、正の整数を入力してください"})

    def testExistValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"値が存在しません、正の整数を入力してください"})

    def testSingleListValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=[1,2,3]")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"値が複数あります、単一の正の整数を入力してください"})

    def testSingleTupleValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=(1,2,3)")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"値が複数あります、単一の正の整数を入力してください"})

    def testSingleDictValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n={'a':1}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"値が複数あります、単一の正の整数を入力してください"})

    def testSingleSetValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n={1,2,3}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"値が複数あります、単一の正の整数を入力してください"})

    def testInteger99999ValueObject(self):
        response = self.app.get("/fibonacci_series/fib?n=99999")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error":"4096桁を超える値の出力はできません、4096桁以下の出力になる正の整数を入力してください"})

if __name__ == "__main__":
    unittest.main()