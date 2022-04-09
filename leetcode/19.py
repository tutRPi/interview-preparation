# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev = self.reverse_list(head)
        if n == 1:
            return self.reverse_list(rev.next)

        curr = rev
        for i in range(n - 2):
            curr = curr.next

        curr.next = curr.next.next
        return self.reverse_list(rev)

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        nxt = head.next
        head.next = None

        while nxt:
            tmp = nxt.next
            nxt.next = head
            head = nxt
            nxt = tmp
        return head