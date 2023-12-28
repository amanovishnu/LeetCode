class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Approach #1
        # output: list = []
        # for i in range(n):
        #     output.append(nums[i])
        #     output.append(nums[n+i])
        # return output
        
        # Approach #2
        for i in range(n, len(nums)):
            nums[i] |= nums[i-n] << 10
        i = 0
        for j in range(n, len(nums)):
            nums[i] = nums[j] >> 10
            nums[i+1] = nums[j] & 1023
            i+=2
        return nums
        
    
# Attempt = AMZN Approach #1
# Time Complexity = O(n) where n is the input 
# Auxilary Space = O(n)
# Space Complexity = O(n)


# Attempt = AMZN Approach #2
# Time Complexity = O(n) where n is the input 
# Auxilary Space = O(1)
# Space Complexity = O(n)