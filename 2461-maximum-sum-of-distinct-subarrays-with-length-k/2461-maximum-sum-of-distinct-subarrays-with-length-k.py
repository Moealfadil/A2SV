class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        unique={}
        current_sum=0
        for i in range(k):
             unique[nums[i]]=unique.get(nums[i],0)+1
             current_sum+=nums[i]
        n=len(nums)
        start=0
        end=k
        max_sum=0
        if len(unique)==k:
                max_sum=max(max_sum,current_sum)
        while end<n:
            current_sum=current_sum-nums[start]+nums[end]
            unique[nums[start]] -= 1
            if unique[nums[start]] == 0:
                del unique[nums[start]]
            unique[nums[end]] = unique.get(nums[end], 0) + 1
            if len(unique)==k:
                max_sum=max(max_sum,current_sum)
            start+=1
            end+=1
        return max_sum
        

        