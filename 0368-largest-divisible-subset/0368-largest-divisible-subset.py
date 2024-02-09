class Solution:
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        if n == 0:
            return []
        
        nums.sort()
        dp = [1] * n
        prev_index = [-1] * n
        maxi = 0
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev_index[i] = j
                    if dp[i] > dp[maxi]:
                        maxi = i
        
        result = []
        while maxi >= 0:
            result.append(nums[maxi])
            maxi = prev_index[maxi]
        
        result.reverse()
        return result