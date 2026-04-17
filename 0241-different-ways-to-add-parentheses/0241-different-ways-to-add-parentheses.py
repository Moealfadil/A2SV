class Solution:
    def diffWaysToCompute(self, expression: str):
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        
        for s in range(len(expression)):
            if expression[s].isdigit():
                continue
            
            left = self.diffWaysToCompute(expression[:s])
            right = self.diffWaysToCompute(expression[s+1:])
            
            for i in left:
                for j in right:
                    if expression[s] == "+":
                        result.append(i + j)
                    elif expression[s] == "*":
                        result.append(i * j)
                    elif expression[s] == "-":
                        result.append(i - j)
        
        return result