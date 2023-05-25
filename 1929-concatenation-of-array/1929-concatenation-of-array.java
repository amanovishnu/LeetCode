class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        output = [0]*2*num_len
        for idx in range(num_len):
            output[idx] = nums[idx]
            output[idx+num_len] = nums[idx]
        return output

# Time Complexity: O(n)
# Space Complexity: O(n)