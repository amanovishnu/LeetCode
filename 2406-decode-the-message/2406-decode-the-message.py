class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        # Approach 1 Using Hashing
        # decoder = {}
        # alpha = 96
        # output = ""
        
        # for idx, ele in enumerate(key):
        #     if ele not in decoder and ele != " ":
        #         alpha += 1
        #         decoder[ele] = chr(alpha)
                
        # for char in message:
        #     output += decoder[char] if char in decoder else " "
            
        # return (output)

        # Apporach 2 Without using Hashing
        index = []
        output = ''

        for ele in key:
            if ele != ' ' and ele not in index:
                index.append(ele)

        for ele in message:
            if ele != ' ':
                output += chr(index.index(ele)+97)
            else:
                output += ' '

        return output