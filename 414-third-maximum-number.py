# First pass solution:
'''
import numpy as np

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inf = 10000
        nums = list(set(nums))
        max_elements = np.ones(3) * -inf

        for i in range(len(nums)):
            if nums[i] >= max_elements[0]:
                max_elements[2] = max_elements[1]
                max_elements[1] = max_elements[0]
                max_elements[0] = nums[i]
            elif nums[i] >= max_elements[1]:
                max_elements[2] = max_elements[1]
                max_elements[1] = nums[i]

            elif nums[i] >= max_elements[2]:
                max_elements[2] = nums[i]

        print(max_elements)
        if max_elements[2] == -inf:
            return int(max_elements[0])
        else:
            return int(max_elements[2])
'''

# Updated solution by taking advantage of max function:
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)

        for i in range(2):
            nums.remove(max(nums))

        return max(nums)