class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result=[]
        while len(arr)>1:
            k=arr.index(max(arr))
            result.append(k+1)
            arr=arr[:k+1][::-1]+arr[k+1:]
            arr=arr[::-1]
            result.append(len(arr))
            arr.pop()
        return result