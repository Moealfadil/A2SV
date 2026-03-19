class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        j=0
        n=len(arr)
        temp=arr.copy()
        while i<n:
            if temp[j]==0:
                arr[i]=0
                i+=1
                if i==n:
                    break
            arr[i]=temp[j]
            j+=1
            i+=1
