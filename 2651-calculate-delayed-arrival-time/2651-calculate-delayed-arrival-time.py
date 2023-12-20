class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        res: int = (arrivalTime+delayedTime)%24
        return res
        