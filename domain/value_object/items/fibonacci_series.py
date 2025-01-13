import os
import sys
import ast

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import elements

class FibonacciSeriesValueObject(elements.ExistValueObject, elements.SingleValueObject, elements.StringValueObject, elements.MinusValueObject, elements.FloatValueObject, elements.IntegerValueObject, elements.MaxSizeValueObject):
    def __init__(self, value=None):
        self.value = value

    def execute_input(self):
        formatting_value = self.typeChange(self.value)
        exist_value = self.existCheck(formatting_value)
        single_value = self.singleCheck(exist_value)
        not_string_value = self.stringCheck(single_value)
        not_minus_value = self.minusCheck(not_string_value)
        not_float_value = self.floatCheck(not_minus_value)
        validation_value = self.integerCheck(not_float_value)
        return validation_value
    
    def execute_output(self):
        max_size_value = self.maxSizeCheck(self.value)
        return max_size_value

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
    
    def maxSizeCheck(self, value):
        return elements.MaxSizeValueObject(value).execute()
    
    def typeChange(self, value):
        if value == '':
            return None
        
        try:
            float_value = float(value)
            if not float_value % 1 == 0:
                return float_value
        except:
            pass
        
        try:
            if float_value:
                return int(float_value)
            return int(value)
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