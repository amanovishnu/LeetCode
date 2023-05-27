class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash = dict()
        for idx in range(len(heights)):
            hash[heights[idx]] = names[idx]
        hash = sorted(hash.items(), reverse=True)
        return [x[1] for x in hash]

# Time Complexity : O(nlogn)
# Space Complexity: O(n)
        