# First try with two dictionaries (O(n) time-complexity, O(n) space-complexity), 56 ms, faster than 34.35%
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        
        intersection_values = set(nums1).intersection(set(nums2))
        
        nums1_dict = dict()
        nums2_dict = dict()
        
        for value in nums1:
            if value in intersection_values:
                if nums1_dict.get(value) is not None:
                    nums1_dict[value] += 1
                else:
                    nums1_dict[value] = 1
        
        for value in nums2:
            if value in intersection_values:
                if nums2_dict.get(value) is not None:
                    nums2_dict[value] += 1
                else:
                    nums2_dict[value] = 1
        
        for key in intersection_values:
            for j in range(min(nums1_dict[key], nums2_dict[key])):
                intersection.append(key)

        
        
        return intersection
            
            