class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0 
        else:
            s = list(s)
            min_ops_1, min_ops_2 = 0, 0
            com_1 = ['1' if x%2==0 else '0' for x in range(len(s))]
            com_2 = ['0' if x%2==0 else '1' for x in range(len(s))]
            for idx in range(len(s)):
                if s[idx] != com_1[idx]:
                    min_ops_1 +=1
                if s[idx] != com_2[idx]:
                    min_ops_2 += 1
            return min(min_ops_1, min_ops_2)