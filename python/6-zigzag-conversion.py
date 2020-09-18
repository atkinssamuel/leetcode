# O(n) time-complexity, O(n) space-complexity, very slow, 436 ms, faster than 8.75%
import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 1:
            return s
        if numRows == 1:
            return s
        mapping_dict = dict()
        row_ind = 0
        col_ind = 0
        letter_ind = 0

        down = True
        
        
        
        while True:
            mapping_dict[letter_ind] = [row_ind, col_ind]
            
            if letter_ind == len(s) - 1:
                break
            
            letter_ind += 1
            
            if down == True and row_ind != numRows - 1:
                row_ind += 1
                continue
        
            if down == True and row_ind == numRows - 1:
                down = False
                row_ind -= 1
                col_ind += 1
                continue
            
            if down == False and row_ind != 0:
                row_ind -= 1
                col_ind += 1
                continue
            
            if down == False and row_ind == 0:
                down = True
                row_ind += 1
                continue
            
        zigzag_matrix = np.array([[None] * (col_ind + 1)] * numRows)
        
        for i in range(len(s)):
            zigzag_matrix[mapping_dict[i][0], mapping_dict[i][1]] = s[i]
        
        output_str = ""
        for element in zigzag_matrix.flatten():
            if element is not None:
                output_str += element
                
        return output_str

# Very clever indexing solution (no need to make a matrix, just add to list of strings), O(n), O(n), 40 ms, faster than 92.36%
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)