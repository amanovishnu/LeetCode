class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        count_frequency = dict()
        target = len(arr)/4

        for ele in arr:
            
            if ele in count_frequency:
                count_frequency[ele] += 1
            else:
                count_frequency[ele] = 1
            
            if count_frequency[ele] > target:
                return ele
        
        return -1
        