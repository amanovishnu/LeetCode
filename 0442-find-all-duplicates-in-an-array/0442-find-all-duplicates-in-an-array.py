class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            n = abs(nums[i])

            if nums[n - 1] < 0:
                result.append(n)
            else:
                nums[n - 1] *= -1

        return result