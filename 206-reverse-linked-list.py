# Iterative solution: 16ms 97.85%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None
        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev

# Recursive solution: 28ms 42.6%
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursiveReverse(self, head, prev):
        next_node = head.next
        head.next = prev
        if next_node is None:
            return head
        else:
            return self.recursiveReverse(next_node, head)

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.recursiveReverse(head, None)
'''