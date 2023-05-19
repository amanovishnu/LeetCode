class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            output = [0]*len(nums)
            l = 0
            r = len(output)-1
            for idx in range(len(nums)):
                if nums[idx]%2 == 0:
                    output[l]=nums[idx]
                    l+=1
                else:
                    output[r]= nums[idx]
                    r-=1
        return output       