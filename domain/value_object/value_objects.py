import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from value_object.integer import IntegerValueObject
from value_object.string import StringValueObject
from value_object.minus import MinusValueObject
from value_object.float import FloatValueObject

ValueObjects = {
    'IntegerValueObject': IntegerValueObject,
    'StringValueObject': StringValueObject,
    'MinusValueObject': MinusValueObject,
    'FloatValueObject': FloatValueObject
}