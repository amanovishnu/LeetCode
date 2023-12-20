class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected: list[int] = sorted(heights)
        idx_count: int = 0
        for idx in range(len(heights)):
            if expected[idx] != heights[idx]:
                idx_count +=1
        return idx_count