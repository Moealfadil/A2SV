class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        satisfied=0
        j=0
        for i in range(len(s)):
            if j==len(g):
                break
            if s[i]>= g[j]:
                satisfied+=1
                j+=1
        return satisfied

        