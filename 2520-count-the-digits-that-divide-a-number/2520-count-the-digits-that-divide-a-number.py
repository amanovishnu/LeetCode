class Solution:
    def countDigits(self, num: int) -> int:
        output: int = 0
        temp: int = num
        while  temp > 0:
            digit: int = temp%10
            if num%digit == 0:
                output += 1 
            temp = temp//10
        return output