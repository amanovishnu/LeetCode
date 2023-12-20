class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_set:set = set()
        for ch in s:
            if ch in char_set:
                return ch
            char_set.add(ch)