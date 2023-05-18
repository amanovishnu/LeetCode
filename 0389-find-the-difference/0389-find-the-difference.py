class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        alpha = [0 for x in range(26)]
        for char in s:
            alpha[ord(char)-97]+=1
        for char in t:
            alpha[ord(char)-97]-=1
        for ele in range(len(alpha)):
            if alpha[ele] != 0:
                return chr(ele+97)