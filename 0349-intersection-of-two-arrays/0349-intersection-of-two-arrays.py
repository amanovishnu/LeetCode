class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        if len(nums1) >= len(nums2):
            min, max = nums2, nums1
        else:
            min, max = nums1, nums2
        output = []
        for ele in min:
            if ele in max:
                output.append(ele)
        return output