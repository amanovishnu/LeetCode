class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        subtree = {}

        for root in arr:
            subtree[root] = 1

            for factor in arr:
                if factor >= root:
                    break
            
                if root % factor == 0 and root // factor in subtree:
                    subtree[root] += subtree[factor] * subtree[root // factor]

        total_trees = sum(subtree.values())
        return total_trees % (10**9 + 7)       