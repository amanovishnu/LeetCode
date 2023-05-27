class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        return nums[2] if len(nums) >=3 else nums[0]
       
# Time Complexity: O(nlogn)
# Space Complexity: O(n)