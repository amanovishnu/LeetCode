class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output: list = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output
    
# Attempt = AMZN
# Time Complexity = O(n) where n is the input 
# Auxilary Space = O(n)
# Space Complexity = O(n)