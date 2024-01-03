class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indices: list = [nums[ele] for ele in range(0, len(nums), 2)]
        odd_indices: list = [nums[ele] for ele in range(1, len(nums), 2)]
        
        even_indices.sort()
        odd_indices.sort(reverse=True)
        
        for idx in range(len(nums)-1, -1, -1):
            if idx%2 ==0:
                nums[idx] = even_indices.pop()
            else:
                nums[idx] = odd_indices.pop()
        return nums