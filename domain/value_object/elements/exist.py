class ExistValueObject:
    def __init__(self, value=None):
        self.value = value

    def execute(self):
        if self.value is None:
            raise ValueError("値が存在しません、正の整数を入力してください")
        
        return self.value