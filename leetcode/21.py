# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list2.val < list1.val:
            list1, list2 = list2, list1
        root = node = list1
        list1 = list1.next

        while True:
            if list1 is None:
                node.next = list2
                break
            if list2 is None:
                node.next = list1
                break

            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        return root