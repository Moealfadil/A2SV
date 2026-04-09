class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        que=deque()
        dic=defaultdict()
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
            while que and dic[s[que[0]]]>1:
                que.popleft()
            que.append(i)
        if dic[s[que[0]]]>1:
            return -1
        else:
            return que[0]
        