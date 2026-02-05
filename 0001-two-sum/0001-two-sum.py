class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for id1, i in enumerate(nums):
            for id2, j in enumerate(nums):
                if id1 == id2:
                    j=+1
                    continue
                elif i+j == target:
                    return [id1,id2]
            i=+1   
        return None