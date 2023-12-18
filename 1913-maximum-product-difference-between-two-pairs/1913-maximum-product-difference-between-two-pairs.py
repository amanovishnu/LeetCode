class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0]*nums[1])-(nums[-2]*nums[-1])