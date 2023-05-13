class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for ele in range(left,right+1):
            if words[ele][0] in vowels and words[ele][-1] in vowels:
                count +=1
        return count