class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix=strs[0]
        for word in strs:
            current_longest_prefix=''
            for letter in range(len(word)):
                if letter<len(longest_prefix) and longest_prefix[letter] == word[letter]:
                    current_longest_prefix += longest_prefix[letter]
                else:
                    break
            longest_prefix=current_longest_prefix
        return longest_prefix

print(Solution().longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"