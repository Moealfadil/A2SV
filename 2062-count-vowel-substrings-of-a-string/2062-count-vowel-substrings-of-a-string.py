class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        vowels = set("aeiou")
        count = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break  # stop if consonant appears
                
                seen.add(word[j])
                
                if len(seen) == 5:
                    count += 1

        return count
            