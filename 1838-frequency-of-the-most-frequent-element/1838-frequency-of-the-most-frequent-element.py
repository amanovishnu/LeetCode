class Solution(object):
    def maxFrequency(self, nums, k):
        maxFrequency = 0  # Initialize the maximum frequency
        currentSum = 0  # Initialize the current sum of the subarray elements

        nums.sort()  # Sort the array in ascending order

        left = 0
        for right in range(len(nums)):
            currentSum += nums[right]  # Include the current element in the subarray sum

            # Check if the current subarray violates the condition (sum + k < nums[right] * length)
            while currentSum + k < nums[right] * (right - left + 1):
                currentSum -= nums[left]  # Adjust the subarray sum by removing the leftmost element
                left += 1  # Move the left pointer to the right

            # Update the maximum frequency based on the current subarray length
            maxFrequency = max(maxFrequency, right - left + 1)

        return maxFrequency