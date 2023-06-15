# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        maxSum = root.val
        ans = 1
        level = 1
        while queue:
            levelSize = len(queue)
            levelSum = 0
            for _ in range(levelSize):
                removed = queue.popleft()
                levelSum += removed.val
                if removed.left:
                    queue.append(removed.left)
                if removed.right:
                    queue.append(removed.right)
            if levelSum > maxSum:
                maxSum = levelSum
                ans = level
            level += 1
        return ans
        