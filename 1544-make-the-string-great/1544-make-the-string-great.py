class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        
        for char in s:
            if res and abs(ord(res[-1]) - ord(char)) == 32:
                res.pop()
            else:
                res.append(char)
                
        return ''.join(res)