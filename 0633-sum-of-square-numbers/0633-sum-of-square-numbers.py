class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i =2
        while i <=sqrt(c):
            if c%i==0:
                count=0
                while c%i==0:
                    count+=1
                    c//=i
                if i%4==3 and count%2!=0:
                    return False
            i+=1
        return c%4!=3
        