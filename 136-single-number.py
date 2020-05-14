# First pass solution: 68ms 85.51%
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1]:
                return nums[i]
            i += 2
        return nums[-1]
