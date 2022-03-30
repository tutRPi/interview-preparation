# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None:
            fast = fast.next
            if fast is None:
                return None
            slow = slow.next
            fast = fast.next
            if slow == fast:
                break
        else:
            return None

        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow