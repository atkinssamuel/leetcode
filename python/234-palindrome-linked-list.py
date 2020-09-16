# Mathematical solution (too slow)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Method:
        # Create a forwards number (that represents the palindrome forward)
        # Create a backwards number
        # Palindrome if they're the same
        if head is None:
            return True
        
        forwards = 0
        backwards = 0
        counter = 0

        while True:
            forwards = forwards * 10 + head.val
            backwards = head.val * pow(10, counter) + backwards
            if head.next is None:
                return forwards == backwards
            head = head.next
            counter += 1

# List flip method, O(n) time-complexity, O(1) space-complexity, 96 ms, faster than 27.34%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        
        fast = slow = head
        
        # Will get slow pointer to exact mid-point
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        
        left_end = slow
        slow = slow.next
        left_end.next = None
        
        # Flipping 2nd half of list
        prev = None
        cur = slow
        nxt = None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
       
        cur = prev
        
        # Comparing list elements for palindrome condition
        while cur:
            if cur.val != head.val:
                return False
            cur = cur.next
            head = head.next
            
        return True
