class SingleValueObject:
    def __init__(self, value, args, kwargs):
        self.value = self.singleCheck(value, args, kwargs)

    def singleCheck(self, value, args, kwargs):
        if args or kwargs:
            raise ValueError("値が複数あります、単一の正の整数を入力してください")

        if isinstance(value, (list, tuple, dict, set)):
            raise ValueError("値が複数あります、単一の正の整数を入力してください")
        
        return value