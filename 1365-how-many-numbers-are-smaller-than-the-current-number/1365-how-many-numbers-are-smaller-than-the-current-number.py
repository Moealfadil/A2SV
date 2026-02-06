class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedList= sorted(nums)
        numLessThan=[]
        for i in nums:
            numLessThan.append(sortedList.index(i))
        return numLessThan

                




        