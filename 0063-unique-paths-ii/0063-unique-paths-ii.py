class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            if A[i][0] == 0:
                ans[i][0] = 1
            else:
                break
        
        for j in range(m):
            if A[0][j] == 0:
                ans[0][j] = 1
            else:
                break
        
        for i in range(1, n):
            for j in range(1, m):
                if A[i][j] == 0:
                    ans[i][j] = ans[i-1][j] + ans[i][j-1]
        
        return ans[n-1][m-1]