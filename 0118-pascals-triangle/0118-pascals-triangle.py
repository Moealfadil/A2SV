class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        base=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            i=2
            while i < numRows:
                current=[]
                current.append(1)
                for num in range(len(base[-1])-1):
                    current.append(base[-1][num]+ base[-1][num+1])
                current.append(1)
                base.append(current)
                i+=1
            return base



        