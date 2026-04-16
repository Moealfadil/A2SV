class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        list1=list(range(1,n+1))
        i=0
        def eliminate(list,k,i):
            if len(list)==1:
                return list[0] 
            i=(i+k-1)%len(list)
            list1.pop(i)
            return eliminate(list,k,i)
        return eliminate(list1,k,i)
        