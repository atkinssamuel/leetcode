# Efficient first pass solution 88.78%

class Solution(object):
    def diStringMatch(self, s):
        """
        :type S: str
        :rtype: List[int]
        """
        result = [0 for i in range(len(s) + 1)]
        upper = len(s)
        lower = 0

        for i in range(len(s)):
            if s[i] == "I":
                result[i] = lower
                lower += 1
            else:
                result[i] = upper
                upper -= 1
            if i == len(s) - 1:
                if s[i] == "I":
                    result[-1] = result[-2] + 1
                else:
                    result[-1] = result[-2] - 1

        return result
