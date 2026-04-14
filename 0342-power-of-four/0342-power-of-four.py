class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1 or n==4:
            return True
        elif n<4:
            return False
        n = self.isPowerOfFour(n/4)
        return n==4 or n==1