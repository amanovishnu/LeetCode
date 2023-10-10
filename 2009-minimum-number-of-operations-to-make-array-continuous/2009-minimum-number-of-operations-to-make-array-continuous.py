class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        queue = deque()
        max_length = 1

        for num in sorted(set(nums)):
            while queue and num - queue[0] >= N:
                queue.popleft()

            queue.append(num)
            max_length = max(max_length, len(queue))

        return N - max_length