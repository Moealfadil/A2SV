class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique={}
        current_sum=0
        max_sum=0
        j=0
        for i in range(len(nums)):
            while nums[i] in unique:
                unique.pop(nums[j])
                current_sum-=nums[j]
                j+=1
            unique[nums[i]]=unique.get(nums[i],0)+1
            current_sum+=nums[i]
            max_sum=max(max_sum,current_sum)
        return max_sum

        