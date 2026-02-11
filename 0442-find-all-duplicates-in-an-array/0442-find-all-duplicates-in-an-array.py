class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        return [x for x in dic if dic[x]==2]
        