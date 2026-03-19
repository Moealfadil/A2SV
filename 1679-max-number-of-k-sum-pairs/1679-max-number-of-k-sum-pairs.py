class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        count=0
        while i<j:
            sum=nums[i]+nums[j]
            if sum==k:
                i+=1
                j-=1
                count+=1
            elif sum<k:
                i+=1
            else:
                j-=1
        return count
        