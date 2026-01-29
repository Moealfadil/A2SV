class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        covered = [False] * 51  # Since the constraints are up to 50

        for start, end in ranges:
            for i in range(start, end + 1):
                covered[i] = True

        for i in range(left, right + 1):
            if not covered[i]:
                return False

        return True
        

        