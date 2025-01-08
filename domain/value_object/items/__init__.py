import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from items.fibonacci_series import FibonacciSeriesValueObject

ValueObjects = {
    'FibonacciSeriesValueObject': FibonacciSeriesValueObject
}