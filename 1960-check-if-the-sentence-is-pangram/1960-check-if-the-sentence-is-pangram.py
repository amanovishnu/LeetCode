class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        alpha_dict = {}
        for ele in range(0,26):
            alpha_dict[chr(ele+97)] = 0
            
        for ele in sentence:
            if ele in alpha_dict:
                alpha_dict[ele] += 1

        return False if 0 in alpha_dict.values() else True