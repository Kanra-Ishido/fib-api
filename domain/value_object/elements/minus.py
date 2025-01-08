class MinusValueObject:
    def __init__(self, value):
        self.value = self.minusCheck(value)

    def minusCheck(self, value):
        if value < 0:
            raise ValueError("負の値が入力されています、正の整数を入力してください")
        
        return value