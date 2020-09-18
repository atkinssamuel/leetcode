# O(n) time-complexity, O(1) space-complexity, 16 ms, faster than 87.35%
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        right_ptr = None
        left_ptr = -1
        
        for i in range(len(s)-1, -1, -1):
            if right_ptr is None and s[i] != " ":
                right_ptr = i
            elif right_ptr is not None:
                if s[i] == " ":
                    return right_ptr - i
        if right_ptr is None:
            return 0
        return right_ptr - left_ptr