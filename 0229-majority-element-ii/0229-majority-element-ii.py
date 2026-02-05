class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        n=len(nums)
        listA=set()
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
            if dic[num]>n/3 :
                listA.add(num)
        return list(listA)       