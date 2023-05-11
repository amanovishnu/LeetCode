class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decoder = {}
        alpha = 96
        output = ""
        for idx, ele in enumerate(key):
            if ele not in decoder and ele != " ":
                alpha += 1
                decoder[ele] = chr(alpha)
                
        for char in message:
            output += decoder[char] if char in decoder else " "
            
        return (output)