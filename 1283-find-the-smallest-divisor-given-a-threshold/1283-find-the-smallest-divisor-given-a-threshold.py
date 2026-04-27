from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div(L,num):
            sumi=0
            for i in range(len(L)):
                sumi+=ceil(L[i]/num)
            return sumi

        nums.sort()
        low=1
        high=nums[-1]
        while low<=high:
            mid=(low+high)//2
            if div(nums, mid)>threshold:
                low=mid+1
            else:
                high=mid-1
        return low
