class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        p = []
        for x in nums:
            heapq.heappush(p, x)
            if len(p) > k:
                heapq.heappop(p)
        return p[0]