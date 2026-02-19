class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        result= [row[:] for row in matrix]
        n=len(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result[j][(n-1)-i]=matrix[i][j]
        matrix[:]=result