class Solution:
    def freqAlphabets(self, s: str) -> str:
        l = len(s)
        output = ""
        while(l>0):
            if s[l-1] == '#':
                output+=chr(int(s[l-1-2: l-1])+96)
                l-=3
            else:
                output+=chr(int(s[l-1])+96)
                l-=1
        return output[::-1]