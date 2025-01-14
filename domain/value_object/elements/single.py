class SingleValueObject:
    def __init__(self, value):
        self.value = value

    def execute(self):
        if isinstance(self.value, (list, tuple, dict, set)):
            raise ValueError("値が複数あります、単一の正の整数を入力してください")
        
        return self.value