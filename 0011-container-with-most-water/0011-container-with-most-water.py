class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxx=0
        i=0
        j=len(height)-1
        while i<j:
            current=min(height[i],height[j])*(j-i)
            maxx=max(maxx,current)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return maxx



