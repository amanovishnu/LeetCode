class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and math.floor(math.log(n)/math.log(4)) == math.ceil(math.log(n)/math.log(4))