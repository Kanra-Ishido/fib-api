class StringValueObject:
    def __init__(self, value):
        self.value = self.stringCheck(value)

    def stringCheck(self, value):
        if isinstance(value, str):
            raise ValueError("文字列が入力されています、正の整数を入力してください")
        
        return value