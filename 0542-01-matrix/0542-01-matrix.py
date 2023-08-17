class Solution:
    def updateMatrix(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(A[0])
        
        if A[0][0] != 0:
            A[0][0] = m + n
        
        # Travel top down
        for j in range(1, m):
            if A[0][j] != 0:
                A[0][j] = A[0][j - 1] + 1
        
        for i in range(1, n):
            if A[i][0] != 0:
                A[i][0] = A[i - 1][0] + 1
        
        for i in range(1, n):
            for j in range(1, m):
                if A[i][j] != 0:
                    A[i][j] = min(A[i - 1][j], A[i][j - 1]) + 1
        
        # Travel up
        for j in range(m - 2, -1, -1):
            if A[n - 1][j] != 0:
                A[n - 1][j] = min(A[n - 1][j], A[n - 1][j + 1] + 1)
        
        for i in range(n - 2, -1, -1):
            if A[i][m - 1] != 0:
                A[i][m - 1] = min(A[i][m - 1], A[i + 1][m - 1] + 1)
        
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if A[i][j] != 0:
                    A[i][j] = min(A[i][j], min(A[i + 1][j], A[i][j + 1]) + 1)
        
        return A