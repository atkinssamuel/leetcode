# First pass solution using array appending: 36ms, 6.57%
import numpy as np


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Element value is the sum of the index at i - 1 and i
        if numRows == 0:
            return []

        returnArray = [[1]]
        previous_row = [1]
        for i in range(2, numRows + 1):
            row = [1 for j in range(i)]
            for j in range(1, i - 1):
                row[j] = previous_row[j - 1] + previous_row[j]
            returnArray.append(row)
            previous_row = row
        return returnArray

