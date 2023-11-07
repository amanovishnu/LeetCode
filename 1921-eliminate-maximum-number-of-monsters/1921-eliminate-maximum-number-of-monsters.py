class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        time=[]
        for i in range(n):
            time.append((dist[i]/speed[i]))
        time.sort()
        for i in range(n):
            if i>=time[i]:
                i-=1
                break
        return i+1 