class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort() # TC: O(nlogn)
        return [idx for idx, ele in enumerate(nums) if ele == target] # TC: O(n)