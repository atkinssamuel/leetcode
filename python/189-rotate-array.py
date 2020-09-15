# Elegant, but time-limit exceeded
def shift(nums):
    return list([nums[-1]]) + nums[:-1]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)

        for i in range(k):
            nums[:] = shift(nums)

# Index remapping method with list clone, O(n) time-complexity, O(n) space-complexity, 92 ms, faster than 29.09%
import numpy as np
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        new_indices = (np.arange(len(nums)) + k%len(nums))%len(nums)
        nums_copy = list(nums)
        
        for i in range(len(nums)):
            nums[new_indices[i]] = nums_copy[i]

