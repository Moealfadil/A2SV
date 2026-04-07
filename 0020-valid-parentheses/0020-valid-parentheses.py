class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        brackets={"(":")", "[":"]","{":"}"}
        for i in s:
            if i in brackets.keys():
                stack.append(i)
            elif len(stack)>0 and brackets[stack[-1]]==i:
                stack.pop(-1)
            else:
                return False
        return len(stack)==0


        