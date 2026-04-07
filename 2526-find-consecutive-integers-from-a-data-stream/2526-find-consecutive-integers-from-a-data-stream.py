class DataStream(object):

    def __init__(self, value, k):
        """
        :type value: int
        :type k: int
        """
        self.value=value
        self.k=k
        self.arr=[]
        self.dic={}

    def consec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        self.dic[num]=self.dic.get(num,0)+1
        self.arr.append(num)
        if len(self.arr)<self.k:
            return False
        else:
            if len(self.arr)>self.k:
                self.dic[self.arr[-(self.k+1)]]-=1
            if self.value in self.dic:
                return self.dic[self.value]==self.k
            else:
                return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)