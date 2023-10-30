class Solution:
    def countBits(num):
        count = 0
        
        while num > 0:
            count += 1
            num &= (num - 1)  # Clear the least significant set bit.
        
        return count

    def sortByBits(self, arr):
        arr.sort(key = lambda num: (Solution.countBits(num), num))
        return arr