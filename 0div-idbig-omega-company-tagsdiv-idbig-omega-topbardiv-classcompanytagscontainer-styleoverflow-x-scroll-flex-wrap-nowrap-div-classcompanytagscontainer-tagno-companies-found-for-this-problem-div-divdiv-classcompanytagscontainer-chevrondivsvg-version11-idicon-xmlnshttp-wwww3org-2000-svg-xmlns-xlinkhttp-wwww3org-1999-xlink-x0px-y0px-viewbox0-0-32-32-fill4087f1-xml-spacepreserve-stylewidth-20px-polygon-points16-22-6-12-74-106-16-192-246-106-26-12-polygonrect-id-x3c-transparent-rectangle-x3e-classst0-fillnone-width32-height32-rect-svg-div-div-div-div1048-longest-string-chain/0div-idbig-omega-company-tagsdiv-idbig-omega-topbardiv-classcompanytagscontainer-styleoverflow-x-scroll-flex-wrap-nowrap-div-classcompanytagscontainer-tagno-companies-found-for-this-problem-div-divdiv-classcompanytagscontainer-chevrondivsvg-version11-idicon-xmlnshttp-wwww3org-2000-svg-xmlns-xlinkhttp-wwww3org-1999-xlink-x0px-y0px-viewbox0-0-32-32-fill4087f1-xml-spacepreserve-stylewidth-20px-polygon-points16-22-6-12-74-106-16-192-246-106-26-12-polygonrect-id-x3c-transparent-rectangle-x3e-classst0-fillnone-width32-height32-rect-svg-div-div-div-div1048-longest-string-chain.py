class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        d = defaultdict(int)                # The keys for d are words. The values    
                                            # are the # of predecessors of that word
        for word in sorted(words,key = len):
            n, d[word] = len(word), 1

            for i in range(n):              # Check which larger words are predecessors
                w = word[:i] + word[i+1:]   # and determine the max length path

                if w in d:
                    d[word] = max(d[word], d[w] + 1)

        return max(d.values())   