class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for char in range(len(s)):
            if s.count(s[char]) ==1:
                return char
        return -1
        