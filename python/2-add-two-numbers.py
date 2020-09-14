# First pass, O(n + m) time-complexity, O(1) space-complexity, 96 ms, faster than 14.28%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        total = 0
        
        if l1 is not None:
            l1_ind = 0
            while True:
                total += l1.val * pow(10, l1_ind)
                if l1.next is None:
                    break
                l1_ind += 1
                l1 = l1.next
        
        if l2 is not None:
            l2_ind = 0
            while True:
                total += l2.val * pow(10, l2_ind)
                if l2.next is None:
                    break
                l2_ind += 1
                l2 = l2.next
        
       
        
        return_list = ListNode()
        return_list_head = return_list
        
        while True:
            return_list.val = total % 10
            total = total // 10
            if total == 0:
                return return_list_head
            return_list.next = ListNode()
            return_list = return_list.next
            
# Carry bit solution:
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	# If either is not present, return the other
    if not (l1 or l2):
        return l1 or l2
		
    node = head = ListNode(None)        
    carry = 0
	
    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        
        carry = sum//10
        sum = sum%10
        node.next = ListNode(sum)
        node = node.next

    return head.next