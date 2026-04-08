class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]
        n=len(temperatures)
        result=[0]*n
        for i in range(n):
            while stack and temperatures[i]> temperatures[stack[-1]]:
                prev_day=stack.pop()
                result[prev_day]=i-prev_day
            stack.append(i)
        return result

