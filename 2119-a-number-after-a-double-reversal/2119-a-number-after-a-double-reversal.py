class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num < 10:
            return True
        else:
            return False if num%10 == 0 else True