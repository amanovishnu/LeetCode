from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_frequency: list = Counter(arr).values()
        return True if len(num_frequency) == len(set(num_frequency)) else False