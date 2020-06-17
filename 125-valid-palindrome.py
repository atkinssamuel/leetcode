# First pass solution without sneaky trick: 5.37%, 384 ms
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pure_str = ""
        if len(s) == 0 or len(s) == 1:
            return True
        for char in s:
            if char.isalnum():
                pure_str += char.lower()
        j = len(pure_str) - 1
        for i in range(len(pure_str)//2):
            print(pure_str[i])
            if pure_str[i] != pure_str[j]:
                return False
            j -= 1
        return True

# Sneaky trick: 98.85%, 24ms
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-z0-9]', '', str(s).lower())
        return s[::-1] == s