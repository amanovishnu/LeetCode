class Solution:
    def subtractProductAndSum(self, n: int) -> int: 
        return self.productOfDigits(n) - self.sumOfDigits(n)
    
    def sumOfDigits(self, n):
        if n < 10: return n
        else: return n%10 + self.sumOfDigits(n//10)
    
    def productOfDigits(self, n):
        if n < 10: return n
        else: return n%10 * self.productOfDigits(n//10)