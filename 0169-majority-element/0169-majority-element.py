class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_nums: int = len(nums)
        if len_nums == 1:
            return nums[0]
        else:
            nums_dict:dict = defaultdict(int)
            for ele in nums:
                nums_dict[ele] += 1
            output:int = [key for key, value in nums_dict.items() if value > floor(len_nums/2)]
            return output[0]
        
        
        # Approach #1 
        # nums_length = len(nums)
        # if nums_length == 1:
        #     return nums[0]
        # else:
        #     nums.sort() # TC: O(nlogn) Uses timsort inplace sorting AS: O(logn)
        #     majority_element_idx: int = floor(nums_length/2) # TC: O(1) len info is stored in metadata
        #     return nums[majority_element_idx] # TC: O(1)

# Analysis Approach 1:    
# 1. Time Complexity: O(nlogn)
# 2. Auxilary Space: O(logn)
# 3. Space Complexity: O(n+logn) 