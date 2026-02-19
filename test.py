def rotate( matrix):
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
        print(matrix)

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
