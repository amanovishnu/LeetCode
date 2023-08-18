class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        indegree = [0] * n
        
        for edge in roads:
            v, w = edge
            indegree[v] += 1
            indegree[w] += 1
            adj[v].add(w)
            adj[w].add(v)
        
        maxdegree = max(indegree)
        
        maxindex = [i for i in range(n) if indegree[i] == maxdegree]
        
        samemaxdegree = len(maxindex)
        
        if samemaxdegree > 1:
            for i in range(1, samemaxdegree):
                for j in range(i):
                    if maxindex[i] not in adj[maxindex[j]]:
                        print(maxindex[i], maxindex[j])
                        return 2 * maxdegree
                    
            return 2 * maxdegree - 1
        
        mxid = maxindex[0]
        max_rank = 0
        
        for j in range(n):
            if j == mxid:
                continue
            rank = maxdegree + indegree[j] - (1 if j in adj[mxid] else 0)
            max_rank = max(max_rank, rank)
            print(mxid)
        
        return max_rank