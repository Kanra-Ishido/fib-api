class NumberItemEntity:
    def __init__(self, number_item):
        self.number_item = number_item

    def toJson(self):
        return {
            'number_item': self.number_item
        }