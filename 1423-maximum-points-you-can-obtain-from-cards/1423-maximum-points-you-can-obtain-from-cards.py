class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        if k >= len(cardPoints):
            return sum(cardPoints)
        prefix=[0]*(len(cardPoints)+1)
        for i in range(1,len(cardPoints)+1):
           prefix[i] =cardPoints[i-1]+ prefix[i-1]
        print(prefix)
        i=0
        j= len(prefix)-1
        count=0
        while k>0:
            if prefix[k+i]- prefix[i] == prefix[j]- prefix[j-k]:
                if cardPoints[i]>=cardPoints[j-1]:
                    count+=cardPoints[i]
                    i+=1
                else:
                    count+=cardPoints[j-1]
                    j-=1
                k-=1
            elif prefix[k+i]- prefix[i] < prefix[j]- prefix[j-k]:
                count+=cardPoints[j-1]
                j-=1
                k-=1
            else:
                count+=cardPoints[i]
                i+=1
                k-=1

        return count
        