class Solution:
    def reverseString(self, s: List[str]) -> None:
        l: str = 0
        r: str = len(s)-1
        while l < r:
            temp: str = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            
# Target: AMZN
# Time Complexity: O(n) 
# Auxilary Space: o(1)
# Space Complexity O(n)