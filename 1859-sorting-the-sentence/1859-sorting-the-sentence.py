class Solution:
    def sortSentence(self, s: str) -> str:
        s_split = s.split()  # TC: O(n)
        res = [0]*len(s_split) # SC: O(n)
        for word in s_split:
            res[int(word[-1])-1] = word[:-1]
        return " ".join(res)
    
# Time Complexity : O(n)
# Space Complexity : O(n)
