class Solution:
    def reorganizeString(self, S):
        char_count = Counter(S)
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        result = []
        prev_count, prev_char = 0, ""
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            prev_count, prev_char = count + 1, char
        return "".join(result) if len(result) == len(S) else ""