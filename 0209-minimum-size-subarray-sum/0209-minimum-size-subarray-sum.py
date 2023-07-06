class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_of_subarray = 0
        min_length = float('inf')
        
        for right in range(len(nums)):
            sum_of_subarray += nums[right]
            
            while sum_of_subarray >= target:
                min_length = min(min_length, right - left + 1)
                sum_of_subarray -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length