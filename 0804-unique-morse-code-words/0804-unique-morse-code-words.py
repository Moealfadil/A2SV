class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet="abcdefghijklmnopqrstuvwxyz"
        dic={}
        seta=set()
        for i in range(26):
            dic[alphabet[i]]=morse_code[i]
        for word in words:
            code=""
            for s in word:
                code += dic[s]
            seta.add(code)
        return len(seta)