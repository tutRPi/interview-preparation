# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        odd_tail = head
        even_head, even_tail = head.next, None

        while odd_tail is not None and odd_tail.next is not None:
            if even_tail:
                even_tail.next = odd_tail.next
            even_tail = odd_tail.next
            odd_tail.next = odd_tail.next.next
            if odd_tail.next is not None:
                odd_tail = odd_tail.next

        if even_tail:
            even_tail.next = None
        odd_tail.next = even_head
        return head
