class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotate=0
        while nums[-1]<nums[0]:
            nums=[nums[-1]]+nums[:-1]
            rotate-=1
        n=len(nums)
        if n==1 and target==nums[0]:
            return 0
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return (rotate+mid)%n
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1