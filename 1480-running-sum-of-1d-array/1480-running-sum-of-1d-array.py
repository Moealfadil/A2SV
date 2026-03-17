class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        running_sum=0
        for i in nums:
            running_sum+=i
            result.append(running_sum)
        return result
        