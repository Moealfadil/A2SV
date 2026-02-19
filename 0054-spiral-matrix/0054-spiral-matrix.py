class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        first_col=0
        first_row=1
        last_col=len(matrix[0])-1
        last_row=len(matrix)-1
        count=1
        i=0
        j=0
        result=[]
        result.append(matrix[i][j])
        while count<((len(matrix[0]))*(len(matrix))):
            while j<last_col and count<((len(matrix[0]))*(len(matrix))):
                j+=1
                result.append(matrix[i][j])
                count+=1
            last_col-=1
            while i< last_row and count<((len(matrix[0]))*(len(matrix))):
                i+=1
                result.append(matrix[i][j])
                count+=1
            last_row-=1
            while j>first_col and count<((len(matrix[0]))*(len(matrix))):
                j-=1
                result.append(matrix[i][j])
                count+=1
            first_col+=1
            while i> first_row and count<((len(matrix[0]))*(len(matrix))):
                i-=1
                result.append(matrix[i][j])
                count+=1
            first_row+=1
        return result
