import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from routes import fibonacci_series_route

Routes = {
    "FibonacciSeriesRoute": fibonacci_series_route
}