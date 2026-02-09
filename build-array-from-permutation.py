class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for num in range(len(nums)):
            ans.append(nums[nums[num]])
        return ans