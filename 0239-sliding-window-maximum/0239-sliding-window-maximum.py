class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_queue=deque()
        result=[]
        for i in range(k):
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()
            max_queue.append(i)
        result.append(nums[max_queue[0]])
        for i in range(k,len(nums)):
            while max_queue and nums[max_queue[-1]]< nums[i]:
                max_queue.pop()
            max_queue.append(i)
            if max_queue[0]<=i-k:
                max_queue.popleft()
            result.append(nums[max_queue[0]])
        return result