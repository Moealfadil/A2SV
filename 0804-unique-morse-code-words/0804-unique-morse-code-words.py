class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet="abcdefghijklmnopqrstuvwxyz"
        dic={}
        lista=[]
        for i in range(26):
            dic[alphabet[i]]=morse_code[i]
        for word in words:
            code=""
            for s in word:
                code += dic[s]
            lista.append(code)
        return len(set(lista))