class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        diff=0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                diff+=1
            count+=diff
        return count

        