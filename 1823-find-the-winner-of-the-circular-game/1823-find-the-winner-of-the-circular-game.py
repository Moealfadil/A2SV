class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        list1=list(range(1,n+1))
        i=0
        while len(list1)>1:
            i=(i+k-1)%len(list1)
            list1.pop(i)
        return list1[0] 
        