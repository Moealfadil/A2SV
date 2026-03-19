class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        max_sum=sum(nums[:k])
        temp=max_sum
        r=k
        l=0
        for i in range(1,n-k+1):
            temp=(temp-nums[l]+ nums[r])
            max_sum=max(temp,max_sum)
            r+=1
            l+=1
        return max_sum/k