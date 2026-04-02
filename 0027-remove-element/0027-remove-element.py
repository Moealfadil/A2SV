class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        occurance= nums.count(val)
        for i in range(occurance):
            nums.remove(val)
        return len(nums)

        