# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode()
        node = root
        carry = 0
        while (l1 and l1.next) or (l2 and l2.next):
            val = carry
            if l1 and l2:
                val += l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val += l1.val
                l1 = l1.next
            elif l2:
                val += l2.val
                l2 = l2.next

            if val > 9:
                val -= 10
                carry = 1
            else:
                carry = 0

            node.val = val
            node.next = ListNode()
            node = node.next

        val = carry + (l1.val + l2.val if l1 and l2 else (l1.val if l1 else l2.val))
        if val > 9:
            node.val = val - 10
            node.next = ListNode()
            node = node.next
            val = 1
        node.val = val

        return root