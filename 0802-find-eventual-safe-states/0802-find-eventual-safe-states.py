class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False] * n
        unsafe = [0] * n

        for i in range(n):
            if unsafe[i] == 0:
                visited[i] = True
                self.dfs(i, visited, graph, unsafe)
                visited[i] = False

        result = []
        for i in range(len(unsafe)):
            if unsafe[i] == 1:
                result.append(i)
        return result

    def dfs(self, node: int, visited: List[bool], graph: List[List[int]], unsafe: List[int]) -> bool:
        isSafe = True
        for neighbor in graph[node]:
            if visited[neighbor] or unsafe[neighbor] == 2:
                isSafe = False
                break
            if unsafe[neighbor] == 1:
                continue
            visited[neighbor] = True
            if not self.dfs(neighbor, visited, graph, unsafe):
                isSafe = False
            visited[neighbor] = False
        unsafe[node] = 1 if isSafe else 2
        return isSafe
