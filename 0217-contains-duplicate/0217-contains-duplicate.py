class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = set()
        for num in nums: # O(1) Time complexity for search
            if num in hash:
                return True
            else:
                hash.add(num)
        return False
        # Overall TC = O(n)
        # Overall SC = O(n) -> for storing num in a set