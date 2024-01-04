class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output: int = 0
        for sentence in sentences:
            output = max(output, sentence.count(" ")+1)
        return output