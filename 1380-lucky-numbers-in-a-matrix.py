# First pass solution: 140ms 19.05%
import numpy as np


class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        matrix = np.array(matrix)
        transpose = matrix.transpose()
        lucky_numbers = []
        for i in range(len(matrix)):
            min_index = np.argmin(matrix[i])
            min_val = np.min(matrix[i])

            max_index = np.argmax(transpose[min_index])

            if max_index == i:
                lucky_numbers.append(min_val)

        return lucky_numbers

