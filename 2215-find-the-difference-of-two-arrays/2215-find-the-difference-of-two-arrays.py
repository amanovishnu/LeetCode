class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1) # O(n)
        set_nums2 = set(nums2) # O(n)
        difference_1 = list(set_nums1 - set_nums2) # O(min(len(set_nums1, set_nums2)))
        difference_2 = list(set_nums2 - set_nums1) # O(min(len(set_nums2, set_nums1)))
        return [difference_1, difference_2]
    
# Time Complexity : O(n+m)
# Space Complexity : O(n+m)

        