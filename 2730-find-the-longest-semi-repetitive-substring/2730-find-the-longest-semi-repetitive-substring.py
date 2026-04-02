class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        max_count = 1
        pair = 0
        idx = 0
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                pair += 1
            
            while pair > 1:
                if s[idx] == s[idx+1]:
                    pair -= 1
                idx += 1
            
            count = i - idx + 1
            max_count = max(max_count, count)
        
        return max_count