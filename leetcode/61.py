# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        # find length (min: 2)
        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next

        k = k % length
        if k == 0:
            return head

        node.next = head
        node = head
        for _ in range(length - k - 1):
            node = node.next
        head = node.next
        node.next = None

        return head