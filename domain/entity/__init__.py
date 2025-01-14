import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from entity.number_item import NumberItemEntity

Entities = {
    'NumberItemsEntity': NumberItemEntity
}