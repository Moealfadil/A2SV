class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(t):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]<t:
                    low=mid+1
                else:
                    high=mid-1
            return low
        start=search(target)
        end=search(target+1)-1

        if start<=end:
            return[start,end]
        else:
            return [-1,-1]