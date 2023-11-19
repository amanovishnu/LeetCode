class Solution(object):
    def reductionOperations(self, nums):
        nums.sort()
        size = len(nums)
        ans = 0
        for i in range(size - 1, 0, -1):
            if nums[i - 1] != nums[i]:
                ans += size - i
        return ans