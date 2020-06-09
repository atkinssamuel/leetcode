# First pass solution: 76ms, 14.27%
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inf = 2147483648
        maxSum = -inf
        curSum = -inf
        for i in range(len(nums)):
            if nums[i] > curSum and curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum