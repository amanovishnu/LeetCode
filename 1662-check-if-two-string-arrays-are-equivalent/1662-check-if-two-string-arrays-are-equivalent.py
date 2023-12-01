class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Apporach 1
        # return "".join(word1) == "".join(word2)
        
        # Time Complexity: O(n+m)
        # Space Complexity: O(1)
        
        # Approach 2         
        string1, string2 = "",""
        for word in word1:
            string1+= word
        for word in word2:
            string2+= word
        return string1 == string2
    
        # Time Complexity: O(n+m)
        # Space Complexity: O()