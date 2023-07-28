class Solution:
    def score(self, nums, l, r, dp):
        if dp[l][r] != -1:
            return dp[l][r]
        if l == r:
            return nums[l]
        
        left = nums[l] - self.score(nums, l + 1, r, dp)
        right = nums[r] - self.score(nums, l, r - 1, dp)
        dp[l][r] = max(left, right)
        
        return dp[l][r]
    
    def PredictTheWinner(self, nums):
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        return self.score(nums, 0, n - 1, dp) >= 0