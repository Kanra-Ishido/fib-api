class SingleValueObject:
    def __init__(self, value):
        self.value = self.singleCheck(value)

    def singleCheck(self, value):
        if isinstance(value, (list, tuple, dict, set)):
            raise ValueError("値が複数あります、単一の正の整数を入力してください")
        
        return value