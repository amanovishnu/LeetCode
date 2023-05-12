class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        for ele in nums:
            dict[ele] = 1 if ele not in dict else dict.get(ele,0)+1
        return sum([x for x in dict.keys() if dict[x] == 1])