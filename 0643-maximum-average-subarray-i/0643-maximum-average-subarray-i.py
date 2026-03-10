class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        avg=sum(nums[:k])/k
        temp=avg
        r=k
        l=0
        for i in range(1,n-k+1):
            temp=(temp*k-nums[l]+ nums[r])/k
            avg=max(temp,avg)
            r+=1
            l+=1
        return avg