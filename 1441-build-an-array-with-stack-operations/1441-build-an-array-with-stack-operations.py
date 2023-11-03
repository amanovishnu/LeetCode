class Solution(object):
    def buildArray(self, target, n):
        result = []
        current = 1  # The current number to be pushed.

        for num in target:
            while current < num:
                # While the current number is less than the target number,
                # push the current number and generate the "Push" operation.
                result.extend(["Push", "Pop"])  # Extend the list with "Push" and "Pop".
                current += 1

            # The current number matches the target number, so push it.
            result.append("Push")

            current += 1  # Move to the next number to be pushed.

        return result