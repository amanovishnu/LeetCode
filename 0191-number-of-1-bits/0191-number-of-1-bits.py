class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while(n!=0):
            output+=(n&1)
            n>>=1
        return output