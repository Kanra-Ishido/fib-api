class MaxSizeValueObject:
    def __init__(self, value):
        self.value = value

    def execute(self):
        max_size = 4096
        if len(str(self.value)) > max_size:
            raise ValueError("4096桁を超える値の出力はできません、4096桁以下の出力になる正の整数を入力してください")
        
        return self.value