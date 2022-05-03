# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return None

        # count
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        head_rev = slow.next
        slow.next = None

        # reverse second half
        nxt = head_rev.next
        head_rev.next = None
        while nxt is not None:
            tmp = nxt.next
            nxt.next = head_rev
            head_rev = nxt
            nxt = tmp

        node = head
        while head_rev is not None and node is not None:
            tmp = node.next
            node.next = head_rev
            tmp2 = head_rev.next
            head_rev.next = tmp
            node = tmp
            head_rev = tmp2