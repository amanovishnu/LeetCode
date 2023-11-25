class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        output = 0
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                output+=1
        return output