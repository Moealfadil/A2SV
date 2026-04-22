class Solution:
    def shipWithinDays(self, weights,days):
        low=max(weights)
        high=sum(weights)
        while True:
            d=1
            curr=0
            mid=(low+high)//2
            for w in weights:
                if w+curr>mid:
                    d+=1
                    curr=0
                curr+=w
            if d>days:
                low=mid+1
            else:
                high=mid
            if low>=high:
                return low