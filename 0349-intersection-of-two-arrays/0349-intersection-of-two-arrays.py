class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        x  = nums1 if len(nums1) <= len(nums2) else nums2
        y = nums1 if len(nums1) > len(nums2) else nums2
        output = list()
        for ele in x:
            if ele in y:
                output.append(ele)
        return output