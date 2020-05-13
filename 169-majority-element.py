# Hash table first past solution:
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        half = math.floor(len(nums) / 2)

        for i in range(len(nums)):
            if count.get(nums[i]) is not None:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
            if count[nums[i]] > half:
                return nums[i]
        return -1
'''

# Solution with array sorting:
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return nums[int(math.floor(len(nums) / 2))]