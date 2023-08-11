class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1): # I updated my code here. (start from c and remove if statement. In the video, start from 1).
                dp[a] += dp[a-c]
        
        return dp[amount]