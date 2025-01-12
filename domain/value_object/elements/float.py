class FloatValueObject:
    def __init__(self, value):
        self.value = value

    def execute(self):
        if isinstance(self.value, float):
            raise ValueError("小数が入力されています、正の整数を入力してください")
        
        return self.value