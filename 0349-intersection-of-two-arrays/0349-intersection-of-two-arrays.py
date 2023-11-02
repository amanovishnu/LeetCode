class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)

        count_dict = dict()

        for ele in nums1: # O(len(num1))
            if ele not in count_dict: # O(1)
                count_dict[ele] = 1
            else:
                count_dict[ele] +=1

        for ele in nums2: # O(len(num2))
            if ele not in count_dict: # O(1)
                count_dict[ele] = 1
            else:
                count_dict[ele] +=1

        return ([x for x,y in count_dict.items() if y>=2]) # O(len(m+n))
        
        
        # Approach #2         
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # x  = nums1 if len(nums1) <= len(nums2) else nums2
        # y = nums1 if len(nums1) > len(nums2) else nums2
        # output = list()
        # for ele in x:
        #     if ele in y:
        #         output.append(ele)
        # return output