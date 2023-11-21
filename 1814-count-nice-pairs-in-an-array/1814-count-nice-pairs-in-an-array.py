class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        nums = [i - int(str(i)[::-1]) for i in nums]
        res = 0
        for n in Counter(nums).values():
            res += n*(n-1)//2 
        return res % (10**9 + 7)