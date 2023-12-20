from collections import defaultdict

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_nums = defaultdict(int, {i:0 for i in range(1, len(nums)+1)})
        for num in nums:
            hash_nums[num] += 1
        
        res = [0,0]
        for key, value in hash_nums.items():
            if value == 2:
                res[0] = key
            if value == 0:
                res[1] = key
        
        return res