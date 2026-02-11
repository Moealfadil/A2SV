class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s=sorted(list(s))
        list_t=sorted(list(t))
        return list_s == list_t
        