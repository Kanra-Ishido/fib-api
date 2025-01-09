import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from service.fibonacci_series import FibonacciSeriesService

Service = {
    "FibonacciSeriesService": FibonacciSeriesService
}