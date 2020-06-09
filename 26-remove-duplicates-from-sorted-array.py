# Clever reverse traversal solution: 84ms, 37.30%
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appeared_set = set()
        count = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] not in appeared_set:
                count += 1
                appeared_set.add(nums[i])
            else:
                nums.pop(i)
        return count