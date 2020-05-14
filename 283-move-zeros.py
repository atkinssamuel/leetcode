# Initial inefficient in-place solution: 2180ms 5.02%
'''
class Solution(object):
    def swap(self, nums, i):
        if i == len(nums) - 1:
            return
        else:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            return self.swap(nums, i+1)

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for element in nums:
            if element == 0:
                zero_count += 1

        i = 0
        while i < len(nums):
            if nums[i] == 0:
                self.swap(nums, i)
                zero_count -= 1
                if zero_count == 0:
                    return
            else:
                i += 1
'''

# Integer indices tracking solution: 40ms 55.88%
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        integer_indices = []
        for i in range(len(nums)):
            if nums[i] != 0:
                integer_indices.append(i)

        if len(integer_indices) == 0:
            return

        for j in range(len(integer_indices)):
            nums[j] = nums[integer_indices[j]]

        nums[len(integer_indices):] = [0] * (len(nums) - len(integer_indices))
'''

# One pass very optimal solution: 32ms 93.34%
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mindex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[mindex] = nums[i]
                mindex += 1

        nums[mindex:] = [0] * (len(nums) - mindex)


