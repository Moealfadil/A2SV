class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        count=0
        i=0
        while i<len(arr):
            if arr[i]>= count+1:
                count+=1
            i+=1
        return count
