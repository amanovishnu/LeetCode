class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash = dict()
        for idx in range(len(heights)):
            hash[heights[idx]] = names[idx]
        sorted_heights = sorted(list(hash.keys()), reverse=True)
        output = []
        for height in sorted_heights:
            output.append(hash.get(height))
        return output
        