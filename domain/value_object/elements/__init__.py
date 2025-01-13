import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from elements.integer import IntegerValueObject
from elements.string import StringValueObject
from elements.minus import MinusValueObject
from elements.float import FloatValueObject
from elements.exist import ExistValueObject
from elements.single import SingleValueObject
from elements.max_size import MaxSizeValueObject

ValueObjects = {
    'IntegerValueObject': IntegerValueObject,
    'StringValueObject': StringValueObject,
    'MinusValueObject': MinusValueObject,
    'FloatValueObject': FloatValueObject,
    'ExistValueObject': ExistValueObject,
    'SingleValueObject': SingleValueObject,
    'MaxSizeValueObject': MaxSizeValueObject
}