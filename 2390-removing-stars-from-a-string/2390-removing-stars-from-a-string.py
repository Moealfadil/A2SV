class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        i=0
        result=[]
        while i<len(s):
            if s[i]=="*":
                result.pop()
            else:
                result.append(s[i])
            i+=1
        return "".join(result)