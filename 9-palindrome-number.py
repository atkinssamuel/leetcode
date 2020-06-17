# First pass reverse string list solution: 82.24%, 48ms
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x = str(x)

        return x == x[::-1]