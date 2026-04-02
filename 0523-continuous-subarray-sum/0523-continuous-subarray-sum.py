class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder={nums[0]%k:0}
        sum=nums[0]
        for i in range(1,len(nums)):
            # nums[i]+=nums[i-1]
            sum+=nums[i]
            if sum==0:
                return True
            if sum%k==0:
                return True
            elif sum%k in remainder:
                if i-remainder[sum%k]>=2:
                    return True
            else:
                remainder[sum%k]=i
        return False


        