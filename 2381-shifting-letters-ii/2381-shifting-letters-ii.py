class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        opp=[0]*(len(s)+1)
        for i in range(len(shifts)):
            if shifts[i][2]==1:
                opp[shifts[i][0]]+=1
                opp[shifts[i][1]+1]-=1
            else:
                opp[shifts[i][0]]-=1
                opp[shifts[i][1]+1]+=1
        print(opp)
        for i in range(1,len(opp)):
            opp[i]=opp[i-1]+opp[i]
        print(opp)
        ordLetter=[]
        for i in range(len(s)):
            ordLetter.append(chr((((ord(s[i])-97+opp[i])%26)+97)))
        return "".join(ordLetter)
        

