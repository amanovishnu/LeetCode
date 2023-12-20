class Solution:
    def numberOfSteps(self, num: int) -> int:
        count: int = 0
        while(num !=0):
            count +=1
            num = num/2 if num%2 == 0 else num-1
        return count