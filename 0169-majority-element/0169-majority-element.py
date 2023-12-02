class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele_dict = {}
        nums_length = len(nums)  # O(n)
        for ele in nums: # O(n)
            if ele in ele_dict.keys(): # O(1)
                ele_dict[ele] += 1
            else:
                ele_dict[ele] = 1
        return (max([key for key, value in ele_dict.items() if value >= nums_length/2]))