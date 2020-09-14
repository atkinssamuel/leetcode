# O(n) time-complexity, O(n) space-complexity, 200 ms, faster than 75.82%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = set()
        
        if headA is None or headB is None:
            return None
        
       
        while True:
            visited.add(id(headA))
            if headA.next is not None:
                headA = headA.next
            else:
                break
        
        while True:
            if id(headB) in visited:
                return headB
            if headB.next is not None:
                headB = headB.next
            else:
                break
        
        return None

# O(n) time-complexity, O(1) space-complexity. 232 ms, faster than 28.30%, 42.7 MB, less than 88.75%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None
        
        AL = 0
        BL = 0
        AP, BP = headA, headB
    
        
        while True:
            AL += 1
            if AP.next is None:
                break
            AP = AP.next
        
        while True:
            BL += 1
            if BP.next is None:
                break
            BP = BP.next

        AP, BP = headA, headB
        
        while AL > BL:
            AP = AP.next
            AL -= 1
        
        while AL < BL:
            BP = BP.next
            BL -= 1
        
        while AL != 0:
            if id(AP) == id(BP):
                return AP
            AP = AP.next
            BP = BP.next
            AL -= 1
        
        return None
        