class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # Apporach 1 Using Hashing
        # alpha_dict = {}
        # for ele in range(0,26):
        #     alpha_dict[chr(ele+97)] = 0
            
        # for ele in sentence:
        #     if ele in alpha_dict:
        #         alpha_dict[ele] += 1

        # return False if 0 in alpha_dict.values() else True

        # Approach 2 Using Lists
        alpha_list = [0 for i in range(26)]

        for ele in sentence:
            alpha_list[ord(ele)-97] = ele
        
        return False if 0 in alpha_list else True