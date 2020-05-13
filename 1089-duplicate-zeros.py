# First pass solution: 236ms 18.93%
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        ignore_next = False
        for i in range(len(arr)-1):
            if arr[i] == 0 and  not ignore_next:
                arr[i+2:] = arr[i+1:-1]
                arr[i+1] = 0
                ignore_next = True
            else:
                ignore_next = False

