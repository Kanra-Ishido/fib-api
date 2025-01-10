import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from application.service import FibonacciSeriesService
from domain.entity import NumberItemEntity
from domain.value_object.items import FibonacciSeriesValueObject

class FibonacciSeriesUsecase:
    def __init__(self, value=None):
        self.value = value

    def calculate(self):
        number_item_validation = FibonacciSeriesValueObject(self.value).value
        number_item = NumberItemEntity(number_item_validation).toJson()['number_item']
        fibonacci_series_service = FibonacciSeriesService(number_item).calculate()
        return fibonacci_series_service