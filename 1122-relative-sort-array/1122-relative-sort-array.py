class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        final=[]
        for i in arr2:
            count=0
            count= arr1.count(i)
            final.extend([i]*count)
        diff=[]
        for i in arr1:
            if i not in arr2:
                diff.append(i)
        for i in sorted(diff):
            final.append(i)
        return final

            


        