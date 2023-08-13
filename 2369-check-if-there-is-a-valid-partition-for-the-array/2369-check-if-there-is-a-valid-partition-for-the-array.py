class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        
        if nums[1] == nums[0]:
            dp[2] = True
        
        for i in range(2, n):
            if nums[i] == nums[i - 1]:
                dp[i + 1] = dp[i + 1] or dp[i - 1]
            
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                dp[i + 1] = dp[i + 1] or dp[i - 2]
            
            if nums[i] == nums[i - 1] + 1 and nums[i] == nums[i - 2] + 2:
                dp[i + 1] = dp[i + 1] or dp[i - 2]
        
        return dp[n]
