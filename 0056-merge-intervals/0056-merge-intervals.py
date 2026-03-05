class Solution:
    def merge(self, intervals):
        i=0
        j=1
        intervals.sort()
        n=len(intervals)
        while j<n:
            if intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
                intervals.pop(j)
                n-=1
            else:
                i+=1
                j+=1
        return intervals