class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        score=0
        while len(nums[0])>0:
            max_num=[]
            for arr in nums:
                max_num.append(max(arr))
                arr.remove(max(arr))
            score+=max(max_num)
        return score
                 

            

        