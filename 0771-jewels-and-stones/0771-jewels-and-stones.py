class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels: set = set(jewels)
        counter: int = 0
        for stone in stones:
            if stone in jewels:
                counter +=1
        return counter
    
# Target: AMZN
# Time Complexity = O(m+n)
# Auxilary Space = O(m)
# Space Complexity = O(m+n)