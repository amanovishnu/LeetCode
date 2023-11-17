class Solution(object):
    def minPairSum(self, nums):
        # Step 1: Sort the array in ascending order
        nums.sort()

        # Step 2: Initialize pointers at the start and end of the sorted array
        left, right = 0, len(nums) - 1

        # Step 3: Initialize a variable to store the minimum of the maximum pair sum
        min_max_pair_sum = float('-inf')

        # Step 4: Iterate until the pointers meet
        while left < right:
            # Step 5: Calculate the current pair sum
            current_pair_sum = nums[left] + nums[right]

            # Step 6: Update the minimum of the maximum pair sum
            min_max_pair_sum = max(min_max_pair_sum, current_pair_sum)

            # Step 7: Move the pointers towards the center
            left += 1
            right -= 1

        # Step 8: Return the minimum of the maximum pair sum
        return min_max_pair_sum