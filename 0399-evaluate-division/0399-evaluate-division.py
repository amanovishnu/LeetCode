from typing import List

class Solution:
    def dfs(self, node: str, dest: str, gr: dict, vis: set, ans: List[float], temp: float) -> None:
        if node in vis:
            return

        vis.add(node)
        if node == dest:
            ans[0] = temp
            return

        for ne, val in gr[node].items():
            self.dfs(ne, dest, gr, vis, ans, temp * val)

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> dict:
        gr = {}

        for i in range(len(equations)):
            dividend, divisor = equations[i]
            value = values[i]

            if dividend not in gr:
                gr[dividend] = {}
            if divisor not in gr:
                gr[divisor] = {}

            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        return gr

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = self.buildGraph(equations, values)
        finalAns = []

        for query in queries:
            dividend, divisor = query

            if dividend not in gr or divisor not in gr:
                finalAns.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(dividend, divisor, gr, vis, ans, temp)
                finalAns.append(ans[0])

        return finalAns