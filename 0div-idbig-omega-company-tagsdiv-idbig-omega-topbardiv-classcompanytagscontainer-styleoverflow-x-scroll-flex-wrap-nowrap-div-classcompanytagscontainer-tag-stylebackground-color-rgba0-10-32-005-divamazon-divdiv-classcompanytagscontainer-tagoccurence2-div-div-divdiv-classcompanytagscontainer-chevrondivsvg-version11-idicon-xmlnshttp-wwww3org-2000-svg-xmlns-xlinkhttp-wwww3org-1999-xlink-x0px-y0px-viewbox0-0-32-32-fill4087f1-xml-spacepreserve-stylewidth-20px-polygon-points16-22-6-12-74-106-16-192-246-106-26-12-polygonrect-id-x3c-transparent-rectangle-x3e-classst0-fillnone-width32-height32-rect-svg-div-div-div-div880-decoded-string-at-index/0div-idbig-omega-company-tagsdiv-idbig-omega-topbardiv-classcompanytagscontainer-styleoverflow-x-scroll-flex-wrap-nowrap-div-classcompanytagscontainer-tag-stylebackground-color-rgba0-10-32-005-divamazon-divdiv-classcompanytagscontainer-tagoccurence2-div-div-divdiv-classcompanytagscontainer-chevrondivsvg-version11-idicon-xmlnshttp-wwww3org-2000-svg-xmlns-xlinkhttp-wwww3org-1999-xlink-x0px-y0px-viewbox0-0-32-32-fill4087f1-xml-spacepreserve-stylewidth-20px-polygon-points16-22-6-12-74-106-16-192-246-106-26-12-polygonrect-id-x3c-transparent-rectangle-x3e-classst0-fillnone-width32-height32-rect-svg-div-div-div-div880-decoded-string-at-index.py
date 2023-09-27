class Solution(object):
    def decodeAtIndex(self, s, k):
        size = 0
        
        # Calculate the size of the decoded string
        for i in range(len(s)):
            if s[i].isdigit():
                size *= int(s[i])
            else:
                size += 1

        # Start decoding from the end of the string
        for i in range(len(s) - 1, -1, -1):
            k = k % size

            if k == 0 and s[i].isalpha():
                return s[i]

            if s[i].isdigit():
                size //= int(s[i])
            else:
                size -= 1

        return ""