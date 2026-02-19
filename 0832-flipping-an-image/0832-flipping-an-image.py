class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in range(len(image)):
            image[row]=image[row][::-1]
            for j in range(len(image)):
                if image[row][j]==0:
                    image[row][j]=1
                else:
                    image[row][j]=0
        return image
