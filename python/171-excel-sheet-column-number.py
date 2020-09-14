# O(n) time-complexity, 20 ms, faster than 73.83%

import string

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        get_index = lambda character : string.lowercase.index(lower(character)) + 1
        
        # general formula:
        # letter_index * 26^i (for each index i)
        total = 0
        s = s[::-1]
        for i in range(len(s)):
            letter_index = get_index(s[i])
            total += letter_index * pow(26, i)
        
        return total