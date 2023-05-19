class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i,j =0,len(nums)-1
        output = set()
        while(i<j):
            output.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(output)