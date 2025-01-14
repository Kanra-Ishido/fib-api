class StringValueObject:
    def __init__(self, value):
        self.value = value

    def execute(self):
        if isinstance(self.value, str):
            raise ValueError("文字列が入力されています、正の整数を入力してください")
        
        return self.value