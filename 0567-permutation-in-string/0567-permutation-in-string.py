class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n=len(s1)
        dic_s1={}
        dic_s2={}
        if len(s1)>len(s2):
            return False

        for i in range(n):
            dic_s1[s1[i]]=dic_s1.get(s1[i],0)+1
            dic_s2[s2[i]]=dic_s2.get(s2[i],0)+1
        if dic_s1==dic_s2:
            return True
        for i in range(n, len(s2)):
            dic_s2[s2[i]]=dic_s2.get(s2[i],0)+1
            dic_s2[s2[i-n]]-=1
            if dic_s2[s2[i-n]]==0:
                dic_s2.pop(s2[i-n])
            if dic_s1==dic_s2:
                return True
        return False

        