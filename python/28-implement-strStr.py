# First pass indexing solution: 20ms, 67.15%
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                found = True
                for j in range(i, i + len(needle)):
                    if haystack[j] != needle[j - i]:
                        found = False
                        break
                if found:
                    return i
        return -1