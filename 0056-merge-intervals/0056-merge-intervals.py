class Solution:
    def merge(self, intervals):
        i=0
        j=1
        intervals.sort()
        n=len(intervals)-1
        result=[]
        last= False
        while j<=n:
            if intervals[i][1]>=intervals[j][0] and j==n:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
                result.append(intervals[i])
                last=True
            elif intervals[i][1]>=intervals[j][0]:
                intervals[i][1]=max(intervals[i][1],intervals[j][1])
            else:
                result.append(intervals[i])
                i=j
            j+=1
        if not last:
            result.append(intervals[j-1])
        return result