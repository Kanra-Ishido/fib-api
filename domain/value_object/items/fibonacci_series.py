import os
import sys
import ast

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import elements

class FibonacciSeriesValueObject(elements.ExistValueObject, elements.SingleValueObject, elements.StringValueObject, elements.MinusValueObject, elements.FloatValueObject, elements.IntegerValueObject):
    def __init__(self, value=None):
        formatting_value = self.typeChange(value)
        exist_value = self.existCheck(formatting_value)
        single_value = self.singleCheck(exist_value)
        not_string_value = self.stringCheck(single_value)
        not_minus_value = self.minusCheck(not_string_value)
        not_float_value = self.floatCheck(not_minus_value)
        self.value = self.integerCheck(not_float_value)

    def existCheck(self, value):
        return elements.ExistValueObject(value).execute()
    
    def singleCheck(self, value):
        return elements.SingleValueObject(value).execute()
    
    def stringCheck(self, value):
        return elements.StringValueObject(value).execute()
    
    def minusCheck(self, value):
        return elements.MinusValueObject(value).execute()
    
    def floatCheck(self, value):
        return elements.FloatValueObject(value).execute()
    
    def integerCheck(self, value):
        return elements.IntegerValueObject(value).execute()
    
    def typeChange(self, value):
        if value == '':
            return None
        
        try:
            return int(value)
        except:
            pass

        try:
            return float(value)
        except:
            pass

        try:
            evaluate_value = ast.literal_eval(value)

            if isinstance(evaluate_value, list):
                return evaluate_value
            elif isinstance(evaluate_value, tuple):
                return evaluate_value
            elif isinstance(evaluate_value, dict):
                return evaluate_value
            elif isinstance(evaluate_value, set):
                return evaluate_value
        except:
            pass

        return value