class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low