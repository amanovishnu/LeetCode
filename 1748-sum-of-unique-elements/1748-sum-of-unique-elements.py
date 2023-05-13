class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict = {}
        sum = 0
        for ele in nums:
            dict[ele] = dict.get(ele,0)+1
        for key in dict.keys():
            if dict[key]==1:
                sum+=key
        return sum