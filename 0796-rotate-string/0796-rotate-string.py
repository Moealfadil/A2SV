class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        current_letter=""
        if len(s)==len(goal):
            for i in range(len(s)):
                if s == goal:
                    return True
                else:
                    current_letter=s[0]
                    s = s[1:]
                    s += current_letter
        return False

        