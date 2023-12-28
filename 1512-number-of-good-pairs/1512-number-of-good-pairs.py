class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Apporach #1
        # if len(nums) == len(set(nums)):
        #     return 0
        # else:
        #     pair_counter: int = 0
        #     for i in range(len(nums)):
        #         for j in range(i+1, len(nums)):
        #             if nums[i] == nums[j]:
        #                 pair_counter += 1
        #     return pair_counter
        
        # Approach #2
        # pairs: dict = defaultdict(int)
        # pair_counter: int = 0
        # for num in nums:
        #     pairs[num] +=1
        # if len(nums) == (len(pairs)):
        #     return 0
        # else:
        #     for value in pairs.values():
        #         pair_counter += value*(value-1)//2
        #     return pair_counter
        
        # Approach #3
        pairs: dict = defaultdict(int)
        pair_counter: int = 0
        for num in nums:
            pair_counter += pairs[num]
            pairs[num] +=1
        return pair_counter
        
# Target: AMZN Approach #1
# Time Complexity: O(n^2)
# Auxilary Space: O(1)
# Space Complexity: O(n)

# Target: AMZN Approach #2
# Time Complexity: O(n+m) in worst case its O(n)
# Auxilary Space: O(m) in worst case its O(n)
# Space Complexity: O(n+m) in worst case its O(n)

# Target: AMZN Approach #3
# Time Complexity: O(n) in worst case its O(n)
# Auxilary Space: O(m) in worst case its O(n)
# Space Complexity: O(n+m) in worst case its O(n)