class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums: list = sorted(nums)
        output: list = []
        for num in nums:
            output.append(sorted_nums.index(num))
        return output