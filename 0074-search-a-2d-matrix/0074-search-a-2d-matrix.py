class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j]==target:
                    return True

        return False