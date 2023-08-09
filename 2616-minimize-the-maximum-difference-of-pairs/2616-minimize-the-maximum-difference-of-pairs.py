class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:

        def pairCtr(mx: int) -> int:                        # Example: nums = [10,1,2,7,1,3]  p = 2
            cnt, idx = 0,1
            while idx < n:                                  #     nums.sort(): [1,1,2,3,7,10]
                if nums[idx] - nums[idx - 1] <= mx:
                    cnt+= 1                                 #            arr = sorted({1-1,2-1,3-2,7-3,10-7})
                    idx+= 1                                 #                = sorted({0,1,4,3})
                idx+= 1                                     #                = [0, 1, 3,4]
            return cnt                                      #                      |
                                                            #      arr[bisect_left(arr, p, key = pairCtr)]

        if p == 0: return 0

        n = len(nums)
        nums.sort()
        arr = sorted({nums[i] - nums[i - 1] for i in range(1, n)})

        return arr[bisect_left(arr, p, key = pairCtr)]