class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)
        j=n-1
        i=0
        count=0
        while count< n//2:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
            count+=1
        return s 

        