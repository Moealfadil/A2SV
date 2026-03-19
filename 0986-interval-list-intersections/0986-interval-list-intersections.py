class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        n=len(firstList)
        m=len(secondList)
        length=min(m,n)
        i,j=0,0
        while i<n and j<m:
            if firstList[i][0]<=secondList[j][1] and firstList[i][1]>=secondList[j][0]:
                result.append([max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])])
            if firstList[i][1]< secondList[j][1] and i+1<n and firstList[i+1][0]<= secondList[j][1]:
                i+=1
            elif firstList[i][1]> secondList[j][1] and j+1<m and firstList[i][1]>= secondList[j+1][0]:
                j+=1
            else:
                i+=1
                j+=1
        return result


        