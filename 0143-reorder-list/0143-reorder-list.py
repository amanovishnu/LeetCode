class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return

        middle = self.midNode(head)
        new_head = middle.next
        middle.next = None

        new_head = self.reverseLinkedList(new_head)

        c1 = head
        c2 = new_head
        f1 = None
        f2 = None

        while c1 and c2:
            # Backup
            f1 = c1.next
            f2 = c2.next

            # Linking
            c1.next = c2
            c2.next = f1

            # Move
            c1 = f1
            c2 = f2

    def midNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        return prev