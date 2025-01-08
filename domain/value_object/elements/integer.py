class IntegerValueObject:
    def __init__(self, value):
        self.value = self.integerCheck(value)

    def integerCheck(self, value):
        if not isinstance(value, int):
            raise ValueError("正の整数を入力してください")
        
        return value