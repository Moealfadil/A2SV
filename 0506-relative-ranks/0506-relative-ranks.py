class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        standing=sorted(score, reverse= True)
        for i in range(len(score)):
            idx=standing.index(score[i])+1
            if idx==1:
                score[i]="Gold Medal"
            elif idx==2:
                score[i]="Silver Medal"
            elif idx==3:
                score[i]="Bronze Medal"
            else:
                score[i]= str(idx)
        return score

        