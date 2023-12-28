class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0
        else:
            pair_counter: int = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] == nums[j]:
                        pair_counter += 1
            return pair_counter
        
# Target: AMZN
# Time Complexity: O(n^2)
# Auxilary Space: O(1)
# Space Complexity: O(n)