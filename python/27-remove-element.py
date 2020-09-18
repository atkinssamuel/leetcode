# Reverse replacement method (O(n) time-complexity, O(1) space-complexity), 20ms, 78.87%
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return nums[0] != val
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != val:
                next_ind = -1
                for j in range(i, -1, -1):
                    if nums[j] == val:
                        next_ind = j
                        break
                if next_ind == -1:
                    return len([element for element in nums if element != val])
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    
        return len([element for element in nums if element != val])
