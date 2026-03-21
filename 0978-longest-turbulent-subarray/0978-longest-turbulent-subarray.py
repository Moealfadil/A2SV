class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 1:
            return 1
        
        # initialize
        if arr[0] == arr[1]:
            higher = None
            count = 1
        else:
            higher = arr[0] > arr[1]
            count = 2
        
        max_count = count
        
        for i in range(2, len(arr)):
            if arr[i] == arr[i-1]:
                count = 1
                higher = None
            else:
                if higher is None:
                    higher = arr[i-1] > arr[i]
                    count = 2
                elif (arr[i-1] < arr[i] and higher) or (arr[i-1] > arr[i] and not higher):
                    count += 1
                    higher = not higher
                else:
                    count = 2
                    higher = arr[i-1] > arr[i]
            
            max_count = max(max_count, count)
        
        return max_count
        





        