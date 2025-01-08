class ExistValueObject:
    def __init__(self, value=None):
        self.value = self.existCheck(value)

    def existCheck(self, value):
        if value is None:
            raise ValueError("値が存在しません、正の整数を入力してください")
        
        return value