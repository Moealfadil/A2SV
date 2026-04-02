class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count=0
        max_count=0
        vowels=set(["a","e","o","i","u"])
        for i in range(k):
            if s[i] in vowels:
                count+=1
        max_count=max(count,max_count)
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1
            max_count=max(count, max_count)
        return max_count
        