class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        output = -1
        for word in range(len(sentence)):
            if sentence[word][: len(searchWord)] == searchWord:
                output = word+1
                break
        return output