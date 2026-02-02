class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners=[]
        losers=[]
        dic_losers={}
        for match in matches:
            winners.append(match[0])
            if match[1]not in dic_losers:
                dic_losers[match[1]]=1
            else:
                dic_losers[match[1]]+=1
        winners=set(winners)
        for loser in dic_losers:
            if loser in winners:
                winners.remove(loser)
            if dic_losers[loser]==1:
                losers.append(loser)
        return [sorted(list(winners)), sorted(losers)]

        