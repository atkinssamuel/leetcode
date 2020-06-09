# First attempt with merge-sort method: 40ms, 9.67%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return
        lr = ListNode()
        lr_head = lr

        while True:
            if l2 is None:
                lr.val = l1.val
                l1 = l1.next
            elif l1 is None:
                lr.val = l2.val
                l2 = l2.next
            elif l1.val < l2.val:
                lr.val = l1.val
                l1 = l1.next
            else:
                lr.val = l2.val
                l2 = l2.next
            if l1 is None and l2 is None:
                break
            else:
                lr.next = ListNode()
                lr = lr.next

        return lr_head

