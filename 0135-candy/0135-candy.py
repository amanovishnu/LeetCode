class Solution:
    def candy(self, ratings) -> int:
        n = len(ratings)  # Get the number of children
        
        candies = [1] * n  # Initialize a list to store the number of candies for each child
        
        # First pass: Check ratings from left to right
        for i in range(1, n):
            if ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                # If the current child has a higher rating and fewer or equal candies than the previous child,
                # give them one more candy than the previous child
                candies[i] = candies[i - 1] + 1
        
        # Second pass: Check ratings from right to left
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                # If the current child has a higher rating and fewer or equal candies than the next child,
                # give them one more candy than the next child
                candies[i] = candies[i + 1] + 1
        
        total_candies = sum(candies)  # Calculate the total number of candies needed
        
        return total_candies