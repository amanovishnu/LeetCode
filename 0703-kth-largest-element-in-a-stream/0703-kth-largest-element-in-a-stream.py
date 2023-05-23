class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.n = k
        for i in nums: self._push(i)
        
    def _push(self, val):
        if len(self.arr) == self.n:
            top = heapq.heappop(self.arr)
            if top > val:
                heapq.heappush(self.arr, top)
            else:
                heapq.heappush(self.arr, val)
        else:
            heapq.heappush(self.arr, val)
    def add(self, val: int) -> int:
        self._push(val)
        return self.arr[0] if len(self.arr) else None