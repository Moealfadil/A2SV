class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        setnum=set()
        for num in nums:
            if num in setnum:
                return True
            else:
                setnum.add(num)
        return False