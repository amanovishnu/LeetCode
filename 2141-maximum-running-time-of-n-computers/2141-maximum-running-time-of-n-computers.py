class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        sumPower = sum(batteries)
        left, right = 1, sumPower // n
        
        while left < right:
            time = (left + right + 1) // 2
            if self.check(batteries, n, time):
                left = time
            else:
                right = time - 1
        return left
    
    def check(self, B: List[int], n: int, time: int) -> bool:
        total_power = sum(min(battery, time) for battery in B)
        return total_power >= time * n