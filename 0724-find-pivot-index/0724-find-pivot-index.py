class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[0]*(len(nums)+1)
        total=sum(nums)
        for i in range(len(nums)):
            prefix[i+1]=nums[i]+prefix[i]
            if prefix[i]==(total-prefix[i]-nums[i]):
                return i
        else:
            return -1