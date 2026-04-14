class Solution:
    def __init__(self):
        self.store={}
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        elif n in self.store:
            return self.store[n]
        ans=self.fib(n-1)+self.fib(n-2)
        self.store[n]=ans
        return ans