class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        stack=[]
        result=[-1]*len(nums)
        i=len(nums)-1
        while i>=0:
            if stack and nums[i]<nums[stack[-1]]:
                result[i]=nums[stack[-1]]
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            stack.append(i)
            i-=1
        i=len(nums)-1
        while i>=0:
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack and nums[i]<nums[stack[-1]]:
                result[i]=nums[stack[-1]]
            stack.append(i)
            i-=1
        return result


            

        