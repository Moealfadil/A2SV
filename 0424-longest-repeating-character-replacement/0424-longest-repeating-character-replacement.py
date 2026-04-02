class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        letters={}
        count=0
        max_count=0
        j=0
        for i in range(len(s)):
            letters[s[i]]=letters.get(s[i],0)+1
            count+=1
            while count-max(letters.values())>k:
                letters[s[j]]-=1
                count-=1
                j+=1
            max_count=max(count,max_count)
        return max_count

                

                
        