class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement,l = max(nums),0
        ans = 0
        count = 0

        for r,num in enumerate(nums):
            if num==maxElement:
                count+=1
            while count==k:
                if nums[l]==maxElement:
                    count-=1
                l+=1
            ans+=l

        return ans