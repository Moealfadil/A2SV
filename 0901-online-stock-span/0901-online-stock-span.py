class StockSpanner:

    def __init__(self):
        
        self.stack=[]
    def next(self, price: int) -> int:
        self.span=1
        self.price=price
        while self.stack and self.stack[-1][0]<=self.price:
            self.span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append([self.price,self.span]) 
        return self.span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)