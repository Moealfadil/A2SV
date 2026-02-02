class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        dic_a={}
        dic_b={}
        for num in a:
            if num not in dic_a:
                dic_a[num]=1
            else:
                dic_a[num]+=1
        for num in b:
            if num not in dic_b:
                dic_b[num]=1
            else:
                dic_b[num]+=1
            
        for num in set(b):
            if num not in dic_a or dic_b[num]>dic_a[num]:
                return False
        return True