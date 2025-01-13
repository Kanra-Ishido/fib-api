import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from domain.value_object.items import FibonacciSeriesValueObject

class FibonacciSeriesService:
    def __init__(self, value):
        self.value = value

    def execute(self):
        if self.value == 0:
            return 0
        
        if self.value == 1:
            return 1
        
        item_n = 1
        item_n_plus1 = 1

        for _ in range(2, self.value):
            item_n, item_n_plus1 = item_n_plus1, item_n + item_n_plus1
            item_n_plus1 = FibonacciSeriesValueObject(item_n_plus1).execute_output()

        return item_n_plus1