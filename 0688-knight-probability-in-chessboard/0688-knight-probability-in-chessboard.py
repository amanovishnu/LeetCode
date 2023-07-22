class Solution:
    def __init__(self):
        self.dp = None
        self.xmove = [-2, -2, -1, -1, 1, 1, 2, 2]
        self.ymove = [-1, 1, -2, 2, -2, 2, -1, 1]

    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:
        self.dp = [[[-1.0 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]
        favourableOutcome = self.solve(row, col, n, k)
        totalOutcome = 8 ** k
        return favourableOutcome / totalOutcome

    def solve(self, row: int, col: int, n: int, k: int) -> float:
        if row < 0 or col < 0 or row >= n or col >= n:
            return 0
        if k == 0:
            return 1
        if self.dp[row][col][k] != -1.0:
            return self.dp[row][col][k]

        ans = 0
        for i in range(8):
            ans += self.solve(row + self.xmove[i], col + self.ymove[i], n, k - 1)

        self.dp[row][col][k] = ans
        return ans
