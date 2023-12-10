class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0]*len(matrix) for x in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                output[j][i] = matrix[i][j]
        return output