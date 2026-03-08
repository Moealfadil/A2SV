class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        num=list(str(num))
        if num[0]== "-":
            num=num[:1]+ sorted(num[1:], reverse= True)
        else:
            num.sort()
            if num[0]=="0":
                for i in range(len(num)):
                    if int(num[i])>0:
                        num[0], num[i]= num[i], num[0]
                        break
        return (int(''.join(num)))
        