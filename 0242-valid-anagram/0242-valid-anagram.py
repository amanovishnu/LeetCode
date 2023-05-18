class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        # Using Arrays
        if(len(s) != len(t)):
            return False
        else:
            array = [0 for x in range(26)]
            for char in s:
                array[ord(char)-97]+=1
            for char in t:
                array[ord(char)-97]-=1
            for ele in array:
                if ele != 0:
                    return False
            return True