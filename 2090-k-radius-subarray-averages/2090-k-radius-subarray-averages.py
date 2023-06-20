class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        windowSize = 2 * k + 1
        ans = [-1] * n
        
        if n < windowSize:
            return ans
        
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]
        
        for i in range(k, n - k):
            ans[i] = (prefixSum[i + k + 1] - prefixSum[i - k]) // windowSize
        
        return ans