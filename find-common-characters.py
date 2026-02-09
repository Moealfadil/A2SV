def commonChars(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters=[]
        for letter in words[0]:
            letters.append(letter)
        for word in words[1:]:
            word= list(word)
            current=[]
            for letter in letters:
                if letter in word:
                    word.remove(letter)
                    current.append(letter)
            letters=current[:]
        return letters

print(commonChars(["bella","label","roller"]))