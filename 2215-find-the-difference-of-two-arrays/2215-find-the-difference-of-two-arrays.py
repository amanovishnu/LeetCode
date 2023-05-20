class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        output = []
        output.append(list(nums1-nums2))
        output.append(list(nums2-nums1))
        return output