class Solution:
    def num_to_digit(self, num:int) -> List[int]:
        digit_list = []
        while(num > 0):
            digit_list.append(num%10)
            num = num//10
        return digit_list[:: -1]

    def separateDigits(self, nums: List[int]) -> List[int]:
        
        # output = []
        # for ele in nums:
        #     output.extend(self.num_to_digit(ele))
        # return output

        output = []
        for ele in nums:
            output.extend([int(x) for x in str(ele)])
        return output