class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [sys.maxsize] * (n + 1)

        dp[0] = 0

        for i, tap_range in enumerate(ranges):
            left = max(0, i - tap_range)
            right = min(n, i + tap_range)

            for j in range(left, right + 1):
                dp[j] = min(dp[j], dp[left] + 1)

        return dp[n] if dp[n] < sys.maxsize else -1