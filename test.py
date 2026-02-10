class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        ans=[]
        for word in words:
            word=word.lower()
            for row in rows:
                if word[0] in row:
                    for char in word:
                        if char not in row:
                            break
                    else:
                        ans.append(word)
        return ans