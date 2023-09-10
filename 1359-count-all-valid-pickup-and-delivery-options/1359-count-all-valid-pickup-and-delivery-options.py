class Solution:
    def __init__(self):
        self.MOD = int(1e9 + 7)  # Modulus for calculations
        self.memoization = []  # Memoization array to store computed values

    def calculateOrdersCount(self, remainingPairs):
        # Base case: No remaining pairs, return 1
        if remainingPairs == 0:
            return 1

        # Check if the value is already computed and return it
        if self.memoization[remainingPairs] != -1:
            return self.memoization[remainingPairs]

        # Calculate the number of valid orders for the remaining pairs
        currentResult = self.calculateOrdersCount(remainingPairs - 1) * (2 * remainingPairs - 1) * remainingPairs % self.MOD

        # Store the result in the memoization array and return it
        self.memoization[remainingPairs] = currentResult
        return currentResult

    def countOrders(self, numPairs):
        # Initialize the memoization array with -1 values
        self.memoization = [-1] * (numPairs + 1)

        # Calculate and return the count of valid orders
        return self.calculateOrdersCount(numPairs)