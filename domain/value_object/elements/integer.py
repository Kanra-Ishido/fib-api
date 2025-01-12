class IntegerValueObject:
    def __init__(self, value):
        self.value = value

    def execute(self):
        if not isinstance(self.value, int):
            raise ValueError("正の整数を入力してください")
        
        return self.value