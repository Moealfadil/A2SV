class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        cano=[]
        unix=path.strip().split("/")
        for i in unix:
            if i=="" or i==".":
                continue
            elif i=="..":
                if cano:
                    cano.pop()
            else:
                cano.append(i)
        return "/"+"/".join(cano)