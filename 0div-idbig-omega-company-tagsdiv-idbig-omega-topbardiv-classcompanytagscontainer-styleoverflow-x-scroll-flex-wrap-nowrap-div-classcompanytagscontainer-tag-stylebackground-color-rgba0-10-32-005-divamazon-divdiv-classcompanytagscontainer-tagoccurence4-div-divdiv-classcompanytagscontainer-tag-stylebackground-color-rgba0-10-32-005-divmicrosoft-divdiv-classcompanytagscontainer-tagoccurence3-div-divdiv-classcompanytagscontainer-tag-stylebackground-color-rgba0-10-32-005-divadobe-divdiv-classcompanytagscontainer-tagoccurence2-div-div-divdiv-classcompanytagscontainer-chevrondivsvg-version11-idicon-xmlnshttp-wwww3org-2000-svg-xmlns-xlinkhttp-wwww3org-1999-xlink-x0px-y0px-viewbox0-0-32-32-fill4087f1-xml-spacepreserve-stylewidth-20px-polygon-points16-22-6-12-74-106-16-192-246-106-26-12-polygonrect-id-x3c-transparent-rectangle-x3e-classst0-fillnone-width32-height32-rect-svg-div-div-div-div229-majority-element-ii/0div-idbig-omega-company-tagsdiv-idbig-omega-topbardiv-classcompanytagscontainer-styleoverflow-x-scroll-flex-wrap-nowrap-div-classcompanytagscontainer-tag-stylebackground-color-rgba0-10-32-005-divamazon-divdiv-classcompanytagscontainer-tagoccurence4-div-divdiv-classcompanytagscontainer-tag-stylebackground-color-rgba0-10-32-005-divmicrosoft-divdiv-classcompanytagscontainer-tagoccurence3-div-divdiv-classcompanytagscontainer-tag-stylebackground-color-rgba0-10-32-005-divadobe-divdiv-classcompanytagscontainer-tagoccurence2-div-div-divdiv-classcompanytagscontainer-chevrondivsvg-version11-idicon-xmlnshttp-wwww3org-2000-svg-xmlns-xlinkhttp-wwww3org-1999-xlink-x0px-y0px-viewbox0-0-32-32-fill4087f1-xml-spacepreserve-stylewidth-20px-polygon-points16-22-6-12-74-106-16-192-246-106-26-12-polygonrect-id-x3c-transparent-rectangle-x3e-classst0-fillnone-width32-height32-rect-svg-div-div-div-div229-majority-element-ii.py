class Solution:
    def majorityElement(self, nums):
        return [num for num, count in Counter(nums).items() if count > len(nums) // 3]