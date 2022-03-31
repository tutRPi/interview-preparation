# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev_head, length = self.copy_reverse_list(head)

        i = 1
        while 2 * i <= length:
            i += 1
            if head.val != rev_head.val:
                return False
            head = head.next
            rev_head = rev_head.next
        return True

    def copy_reverse_list(self, head: Optional[ListNode]) -> (Optional[ListNode], int):
        if head is None:
            return (None, 0)

        count = 1
        nxt = head.next
        head = ListNode(head.val)
        while nxt:
            count += 1
            head_tmp = head
            head = ListNode(nxt.val)
            head.next = head_tmp
            nxt = nxt.next

        return (head, count)