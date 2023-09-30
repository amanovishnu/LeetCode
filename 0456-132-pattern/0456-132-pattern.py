class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []  # Stack for potential '2' elements.
        s3 = float('-inf')  # Initialize potential '3' element.

        for num in reversed(nums):
            if num < s3:
                return True  # Found '1' element.

            while stack and num > stack[-1]:
                s3 = stack.pop()  # Update potential '3'.

            stack.append(num)  # Push elements.

        return False  # No '132' pattern found.