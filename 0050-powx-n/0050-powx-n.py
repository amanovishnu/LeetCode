class Solution:
    def myPow(self, x: float, n: int) -> float:

        def bs(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = bs(x, n//2)
            res = res * res
            if n % 2:
                return res * x
            else: 
                return res


        res = bs(x, abs(n)) 
        if n >= 0: return res
        return 1/res