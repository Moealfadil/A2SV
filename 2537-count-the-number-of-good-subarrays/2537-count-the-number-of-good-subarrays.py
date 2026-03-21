from collections import defaultdict
class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)
        pairs = 0
        result = 0
        l = 0
        for r in range(len(nums)):
            pairs += freq[nums[r]]
            freq[nums[r]] += 1
            while pairs >= k:
                result += len(nums) - r
                freq[nums[l]] -= 1
                pairs -= freq[nums[l]]
                l += 1
        return result


        