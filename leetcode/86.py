# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_small, head_greater = None, None
        smaller, greater = None, None

        node = head
        while node is not None:
            copy = ListNode(node.val)
            if node.val < x:
                if head_small is None:
                    head_small = copy
                else:
                    smaller.next = copy
                smaller = copy
            else:
                if head_greater is None:
                    head_greater = copy
                else:
                    greater.next = copy
                greater = copy

            node = node.next

        if head_small is None:
            return head_greater
        else:
            smaller.next = head_greater
            return head_small

