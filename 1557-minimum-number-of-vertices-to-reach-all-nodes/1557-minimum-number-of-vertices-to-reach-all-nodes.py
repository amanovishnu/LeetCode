class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        return list(set(range(n)) - set(j for i, j in edges))