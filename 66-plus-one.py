# First attempt solution without recursion: 68ms, 5.05%
import numpy as np

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -2, -1):
            if i == -1:
                return_list = np.zeros(len(digits) + 1, dtype=int)
                return_list[1:] = digits
                return_list[0] = 1
                return return_list
            elif digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0