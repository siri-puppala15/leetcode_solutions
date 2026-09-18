class Solution(object):
    def maximalSquare(self, matrix):
        s = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        matrix[i][j] = 1 
                    else: 
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    s = max(s,matrix[i][j])
                else:
                    matrix[i][j]=0
        return s*s