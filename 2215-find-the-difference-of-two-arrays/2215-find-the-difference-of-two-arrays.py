class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        output.append(self.find_difference(nums1, nums2))
        output.append(self.find_difference(nums2, nums1))
        return output

    
    def find_difference(self, n1, n2):
        n1 = set(n1)
        n2 = set(n2)
        res = []
        for n in n1:
            if n not in n2:
                res.append(n)
        return res
        