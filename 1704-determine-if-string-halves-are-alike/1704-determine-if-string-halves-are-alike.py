class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Short Code Based Approach         
        # vowels = {"a","e","i","o","u"}
        # v1 = list(filter(lambda x: x.lower() in vowels, s[:len(s)//2]))
        # v2 = list(filter(lambda x: x.lower() in vowels, s[len(s)//2:]))
        # return True if len(v1) == len(v2) else False
        
        #Optimized Apporach
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        # lCount, rCount = 0,0
        # left, right = 0, len(s)-1
        # while(left <right):
        #     lCount += 1 if s[left] in vowels else 0
        #     rCount += 1 if s[right] in vowels else 0
        #     left+=1
        #     right-=1
        # return lCount==rCount
        
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        a_count, b_count = 0, 0
        for i in range(len(a)):
            if a[i] in vowels:
                a_count += 1
            if b[i] in vowels:
                b_count += 1
        return a_count == b_count