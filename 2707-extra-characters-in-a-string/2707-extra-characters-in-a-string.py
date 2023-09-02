class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        max_len = len(s) + 1  # Maximum length of a valid substring
        dp = [max_len] * (max_len)  # Initialize an array to store minimum extra characters needed for substrings
        
        dp[0] = 0  # No extra characters needed for an empty string
        word_set = set(dictionary)  # Convert the dictionary into a set for efficient word look-up
        
        for i in range(1, max_len):
            dp[i] = dp[i - 1] + 1  # Initialize with a worst-case scenario (one more character than previous)
            
            for length in range(1, i + 1):
                # Check if the substring s[i-length:i] exists in the dictionary
                if s[i - length:i] in word_set:
                    # If it does, update dp[i] with the minimum of current dp[i] and dp[i-length]
                    dp[i] = min(dp[i], dp[i - length])
                    
        return dp[-1]  # Return the minimum extra characters needed for the entire string