class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        result=s[:]
        for i in range(len(s)):
            if indices[i]==0:
                result= s[i]+ result[1:]
            elif indices[i]== len(s):
                result=result[:len(s)] + s[i]
            else:
                result= result[:indices[i]] +s[i] + result[indices[i]+1:]
        return result


        