class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        total=0
        i=0
        j=0
        while j<len(nums) and (nums[i]+nums[j])<target :
                j+=1
        j-=1
        while i<j:
            if nums[i]+nums[j]<target:
                total+= j-i
                i+=1
            else:
                j-=1
        return total
        
            
        