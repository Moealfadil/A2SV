class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        result=[]
        for i in range(len(logs)):
            if logs[i]=="../":
                if result:
                    result.pop()
            elif logs[i]!="./":
                result.append(logs[i]) 
        return len(result)