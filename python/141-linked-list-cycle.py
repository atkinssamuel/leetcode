# First pass solution (O(N) space-time), 64ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        
        if head is None:
            return False
        
        while head.next is not None:
            if id(head) in visited:
                return True
            else:
                visited.add(id(head))
                head = head.next    
        
        return False


# O(1) space-time, 40 ms, faster than 75.36%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        fast = head
        slow = head
        
        while fast.next is not None and fast.next.next is not None and slow.next is not None:
            fast = fast.next.next
            slow = slow.next
            
            if id(fast) == id(slow):
                return True
        
        return False