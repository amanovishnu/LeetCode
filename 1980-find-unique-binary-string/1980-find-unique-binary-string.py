class Solution:
    def binGenerate(self, curr, n, binSet):
        if len(curr) == n:
            if curr not in binSet:
                return curr
            return ""

        addZero = self.binGenerate(curr + "0", n, binSet)
        if addZero:
            return addZero

        return self.binGenerate(curr + "1", n, binSet)

    def findDifferentBinaryString(self, nums):
        n = len(nums)
        binSet = set(nums)

        return self.binGenerate("", n, binSet)