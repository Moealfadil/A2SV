class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        n=len(tokens)
        for i in range(n):
            if tokens[i]=="+":
                result=stack[-2]+stack[-1]
                stack.pop()
                stack[-1]=result
            elif tokens[i]=="-":
                result=stack[-2]-stack[-1]
                stack.pop()
                stack[-1]=result
            elif tokens[i]=="/":
                result=int(stack[-2]/stack[-1])
                stack.pop()
                stack[-1]=result
            elif tokens[i]=="*":
                result=stack[-2]* stack[-1]
                stack.pop()
                stack[-1]=result
            else:
                stack.append(int(tokens[i]))
        return stack[0]