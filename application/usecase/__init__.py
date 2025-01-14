import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from usecase.fibonacci_series import FibonacciSeriesUsecase

Usecase = {
    "FibonacciSeriesUsecase": FibonacciSeriesUsecase
}