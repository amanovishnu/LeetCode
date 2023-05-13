class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a","e","i","o","u"}
        v1 = list(filter(lambda x: x.lower() in vowels, s[:len(s)//2]))
        v2 = list(filter(lambda x: x.lower() in vowels, s[len(s)//2:]))
        return True if len(v1) == len(v2) else False