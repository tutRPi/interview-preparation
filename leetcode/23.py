# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)
        if size == 0:
            return None
        elif size == 1:
            return lists[0]
        elif size == 2:
            l, r = lists[0], lists[1]
            if l is None: return r
            if r is None: return l

            if l.val <= r.val:
                head = l
                l = l.next
            else:
                head = r
                r = r.next

            node = head
            while l and r:
                if l.val <= r.val:
                    node.next = l
                    l = l.next
                else:
                    node.next = r
                    r = r.next
                node = node.next

            if l:
                node.next = l
            else:
                node.next = r

            return head
        else:
            left = self.mergeKLists(lists[:size // 2])
            right = self.mergeKLists(lists[size // 2:])
            return self.mergeKLists([left, right])