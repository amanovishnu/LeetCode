class Solution:
    MAX_TARGET = 1010  # Maximum possible target value

    def __init__(self):
        self.dp = [-1] * Solution.MAX_TARGET  # Array to store computed results

    def countCombinations(self, nums, remainingTarget):
        # If the remaining target is 0, there's one valid combination.
        if remainingTarget == 0:
            return 1
        
        # If the remaining target becomes negative, it's not possible to reach it.
        if remainingTarget < 0:
            return 0
        
        # If the result for 'remainingTarget' is already computed, return it.
        if self.dp[remainingTarget] != -1:
            return self.dp[remainingTarget]
        
        currentCombinations = 0
        
        # Iterate through the numbers in 'nums'.
        for currentNum in nums:
            # Recursively calculate combinations for the new target.
            currentCombinations += self.countCombinations(nums, remainingTarget - currentNum)
        
        # Store and return the computed result.
        self.dp[remainingTarget] = currentCombinations
        return currentCombinations

    def combinationSum4(self, nums, target):
        # Start the combination count calculation.
        return self.countCombinations(nums, target)