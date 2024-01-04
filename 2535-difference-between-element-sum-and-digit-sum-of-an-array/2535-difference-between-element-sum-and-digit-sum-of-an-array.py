class Solution:
    
    def sumOfDigits(self, num: int) -> int:
        if num < 10: return num
        else: return num%10 + self.sumOfDigits(num//10)
    
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums)-sum([self.sumOfDigits(x) for x in nums]))