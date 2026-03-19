class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        i=0
        while i<len(s):
            if not s[i].isalnum():
                s.pop(i)
            else:
                i+=1
        s = ''.join(c for c in s)
        s = s.lower()
        return s == s[::-1]
        