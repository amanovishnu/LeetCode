from collections import defaultdict

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_dict = defaultdict(int)
        for ele in arr:
            arr_dict[ele] += 1
        for ele in arr_dict.keys():
            if ele == 0 and arr_dict[ele] >= 2:
                return True
            elif ele*2 in arr_dict and ele != 0:
                return True
        return False