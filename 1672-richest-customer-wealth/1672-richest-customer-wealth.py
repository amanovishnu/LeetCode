class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth: int = -1
        for account in accounts:
            sum_of_wealth: int = 0
            for wealth in account:
                sum_of_wealth += wealth
            max_wealth = max(sum_of_wealth, max_wealth)
        return max_wealth
    
    
# Attempt: AMZN
# Time Complexity = O(m*n)
# Auxilary space = O(1)
# Space Complexity = O(1) 