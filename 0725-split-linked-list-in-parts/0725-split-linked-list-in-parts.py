# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        ans = [None] * k
        x = n // k

        curr = head
        for i in range(k):
            realSize = x
            if i < n % k:
                realSize += 1
            if realSize == 0:
                ans[i] = None
                continue

            ans[i] = curr

            for j in range(realSize - 1):
                curr = curr.next

            temp = curr
            curr = curr.next
            temp.next = None

        return ans