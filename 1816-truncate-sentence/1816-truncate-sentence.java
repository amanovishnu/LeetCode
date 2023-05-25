class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for idx, ch in enumerate(s):
            if ch == " ":
                k-=1
            if k == 0:
                return s[:idx]
        return s

# Time Complexity: O(n)
# Space Complexity: O(1)