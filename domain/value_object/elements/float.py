class FloatValueObject:
    def __init__(self, value):
        self.value = self.floatCheck(value)

    def floatCheck(self, value):
        if isinstance(value, float):
            raise ValueError("小数が入力されています、正の整数を入力してください")
        
        return value