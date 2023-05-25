class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(1,len(nums)):
            nums[idx] = nums[idx-1]+nums[idx]
        return nums

# Time Complexity: O(n)
# Space Complexity: O(1)