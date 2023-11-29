class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n!=0:
            cnt += (n % 2)
            n >>= 1
        return cnt
