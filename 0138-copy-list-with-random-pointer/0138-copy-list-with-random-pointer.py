"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':    
        hash = {None:None}
        cur = head
        
        while cur:
            hash[cur] = Node(cur.val)
            cur = cur.next
            
        cur = head
        
        while cur:
            copy = hash[cur]
            copy.next = hash[cur.next]
            copy.random = hash[cur.random]
            cur = cur.next
            
        return hash[head]