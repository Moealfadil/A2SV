class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic={}
        n=len(intervals)
        res=[]
        max_end=0
        for i in range(n):
            dic[intervals[i][0]]=i
            max_end=max(max_end,intervals[i][1])
        starts=sorted(dic.keys())
        for i in range(n):
            if intervals[i][1]>starts[-1]:
                res.append(-1)
            else:
                x=dic[starts[bisect_left(starts,intervals[i][1])]]
                res.append(x) 
        return res
