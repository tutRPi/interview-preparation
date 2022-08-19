# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        one = head
        new_head = head.next
        one.next = new_head.next
        new_head.next = one

        node = one
        while node is not None and node.next is not None and node.next.next is not None:
            one = node.next
            two = node.next.next
            one.next = two.next
            two.next = one

            node.next = two
            node = one

        return new_head