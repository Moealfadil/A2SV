class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(n)>1:
            if abs(n)%2==0:
                result=self.myPow(x,n/2)
                return result*result
            elif n>0:
                result=self.myPow(x,int(n/2))
                return result*result*x
            else:
                result=self.myPow(x,int(n/2))
                return result*result*1/x
        if n>=0:
            if n==1:
                return x
            elif n==0:
                return 1
            return self.myPow(x,n-1)*x
        else:
            if n==-1:
                return 1/x
            return self.myPow(x,n+1)*(1/x)