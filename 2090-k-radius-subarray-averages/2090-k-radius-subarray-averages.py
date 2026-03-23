class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result=[-1]*len(nums)
        num_sum=sum(nums[:2*k+1])
        for i in range(2*k,len(nums)):
            result[i-k]= num_sum//(2*k+1)
            if i+1>=len(nums):
                break
            num_sum-=nums[i-2*k]
            num_sum+=nums[i+1]
        return result