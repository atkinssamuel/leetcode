# First pass solution: 12ms 96.67%
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        S = S.split()

        return_string = ""

        for i in range(len(S)):
            if S[i][0] in vowel_set:
                return_string += S[i] + "ma"
            else:
                return_string += S[i][1:] + S[i][0] + "ma"
            return_string += "a" * (i + 1)

            if i != len(S) - 1:
                return_string += " "

        return return_string
