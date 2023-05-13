class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num%10==0:
                if math.floor(math.log10(num)+1)%2 == 0:
                    count += 1 
            else:
                if num != 1 and math.ceil(math.log10(num))%2 == 0:
                    count+=1
        return count