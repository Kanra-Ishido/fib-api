class FibonacciSeriesService:
    def __init__(self, value):
        self.value = value

    def calculate(self):
        if self.value == 0:
            return 0
        
        if self.value == 1:
            return 1
        
        item_n = 1
        item_n_plus1 = 1

        for _ in range(2, self.value):
            item_n, item_n_plus1 = item_n_plus1, item_n + item_n_plus1

        return item_n_plus1