class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        i = 1
        n = len(self.stack) - 1
        while n >= 0 and self.stack and price >= self.stack[n]:
            i += 1
            n -= 1
        self.stack.append(price)
        return i
    

            


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)