from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if len(Counter(sentence).keys()) == 26 else False