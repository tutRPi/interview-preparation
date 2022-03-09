# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        slow, fast = head, head.next
        while fast.next is not None and fast.next.next is not None:
            slow, fast = slow.next, fast.next.next

        mid = slow.next

        node = TreeNode(mid.val)
        slow.next = None
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node