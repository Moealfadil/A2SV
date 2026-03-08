class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        p=0
        t=0
        while t<len(trainers) and p<(len(players)):
            if players[p]<= trainers[t]:
                p+=1
            t+=1
        return p