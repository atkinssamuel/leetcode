# First pass solution: 88ms 24.34%
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        duplicates = set()
        elements = {}
        for i in range(len(nums)):
            if elements.get(nums[i]) is None:
                elements[nums[i]] = 1
            else:
                duplicates.add(nums[i])

        for i in range(len(nums)):
            if nums[i] in duplicates:
                for j in range(i+1, min(i+1+k, len(nums))):
                    if nums[i] == nums[j]:
                        return True
        return False

