from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = Counter(s)
        result = sorted(s, key=lambda x: (counter[x], x), reverse=True)
        return "".join(result)

print(Solution().frequencySort("loveleetcode"))
