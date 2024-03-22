class Solution:
    def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        reverse_head = self.reverse(slow)
        temp1 = head
        temp2 = reverse_head
        
        while temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        
        return True