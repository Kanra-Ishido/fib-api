import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import elements

class FibonacciSeriesValueObject(elements.ExistValueObject, elements.SingleValueObject, elements.StringValueObject, elements.MinusValueObject, elements.FloatValueObject, elements.IntegerValueObject):
    def __init__(self, value=None):
        exist_value = self.existCheck(value)
        single_value = self.singleCheck(exist_value)
        not_string_value = self.stringCheck(single_value)
        not_minus_value = self.minusCheck(not_string_value)
        not_float_value = self.floatCheck(not_minus_value)
        self.value = self.integerCheck(not_float_value)

    def existCheck(self, value):
        return elements.ExistValueObject(value).value
    
    def singleCheck(self, value):
        return elements.SingleValueObject(value).value
    
    def stringCheck(self, value):
        return elements.StringValueObject(value).value
    
    def minusCheck(self, value):
        return elements.MinusValueObject(value).value
    
    def floatCheck(self, value):
        return elements.FloatValueObject(value).value
    
    def integerCheck(self, value):
        return elements.IntegerValueObject(value).value