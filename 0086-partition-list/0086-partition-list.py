# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        current = head  # Pointer to traverse the original list
        
        less_dummy = ListNode(0)    # Dummy node for nodes < x
        less_tail = less_dummy           # Tail pointer for less list
        
        greater_dummy = ListNode(0) # Dummy node for nodes >= x
        greater_tail = greater_dummy     # Tail pointer for greater list
        
        # Traverse the original list
        while current:
            if current.val < x:
                # Append current node to the less list
                less_tail.next = ListNode(current.val)
                less_tail = less_tail.next  # Move the tail pointer
            else:
                # Append current node to the greater list
                greater_tail.next = ListNode(current.val)
                greater_tail = greater_tail.next  # Move the tail pointer
            current = current.next  # Move to the next node
        
        
        # Attach the greater list to the end of the less list
        less_tail.next = greater_dummy.next
        
        # Return the modified list starting from the first node after the less dummy node
        return less_dummy.next
        