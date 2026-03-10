class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        unique=set()
        n=len(s)
        i=0
        j=0
        while j<n:
            if s[j] not in unique:
                unique.add(s[j])
                j+=1
            else:
                unique.remove(s[i])
                i+=1
            length=max(len(unique), length)
        return length