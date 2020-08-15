# First pass solution: 48.94%, 20ms
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_count = 0

        for i in range(min(2, len(s))):
            if s[i] == "A":
                if a_count == 1:
                    return False
                else:
                    a_count = 1

        if len(s) <= 2:
            return True

        for i in range(2, len(s)):
            if s[i] == "L" and s[i - 1] == "L" and s[i - 2] == "L":
                return False
            elif s[i] == "A":
                if a_count == 1:
                    return False
                else:
                    a_count = 1
        return True