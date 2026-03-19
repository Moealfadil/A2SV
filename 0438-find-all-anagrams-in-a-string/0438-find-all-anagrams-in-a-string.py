from collections import Counter 
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n=len(p)
        dic_p=Counter(p)
        result=[]
        dic_s=Counter(s[:n])
        if dic_s == dic_p:
                result.append(0)
        for i in range(len(s)-n):
            if s[i+n] in dic_s:
                dic_s[s[i+n]]+=1
            else:
                dic_s[s[i+n]]=1
            if dic_s[s[i]]>1:
                dic_s[s[i]]-=1
            else:
                dic_s.pop(s[i])
            if dic_s == dic_p:
                result.append(i+1)
        return result