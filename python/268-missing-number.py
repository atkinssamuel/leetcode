# First pass solution taking advantage of sets, 268 ms, faster than 13.91%
import numpy as np

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reqs = set(np.arange(max(nums)))
        diff = reqs.difference(set(nums))
        if len(list(diff)) == 0:
            return len(nums)
        else:
            return diff.pop()

# Clever total solution, O(n) time-complexity, O(1) space-complexity, 112 ms, faster than 91.34%
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        req_max = len(nums) + 1
        req_total = 0
        
        for i in range(req_max):
            req_total += i
        
        
        total = sum(nums)
                
        return req_total - total