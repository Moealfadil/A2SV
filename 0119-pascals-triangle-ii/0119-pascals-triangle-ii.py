class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        base=[[1],[1,1]]
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            i=2
            while i <= rowIndex:
                current=[]
                current.append(1)
                for num in range(len(base[-1])-1):
                    current.append(base[-1][num]+ base[-1][num+1])
                current.append(1)
                base.append(current)
                i+=1
            return base[rowIndex]