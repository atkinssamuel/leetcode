# First attempt: 56ms, 22.76%
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                if (s[i+1] == "V" or s[i+1] == "X") and s[i] == "I":
                    total -= numeral_dict[s[i]]
                    continue
                if (s[i+1] == "L" or s[i+1] == "C") and s[i] == "X":
                    total -= numeral_dict[s[i]]
                    continue
                if (s[i+1] == "D" or s[i+1] == "M") and s[i] == "C":
                    total -= numeral_dict[s[i]]
                    continue
            total += numeral_dict[s[i]]
        return total