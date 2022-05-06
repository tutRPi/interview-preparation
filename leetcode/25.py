# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 1:
            return head

        node = head
        n = 1
        while node.next is not None:
            node = node.next
            n += 1

        new_head, prev = None, None
        for _ in range(n // k):

            tmp_head = head
            nxt = head.next

            for i in range(k - 1):
                tmp = nxt.next
                nxt.next = head
                head = nxt
                nxt = tmp

            if new_head is None:
                new_head = head

            tmp_head.next = nxt
            if prev:
                prev.next = head
            prev = tmp_head
            head = nxt

        return new_head