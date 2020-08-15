# First attempt: 36ms, 10.43%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        ref_word = strs.pop(0)

        return_string = ""

        for i in range(len(ref_word)):
            matching = True
            for word in strs:
                if i >= len(word):
                    return return_string

                if word[i] != ref_word[i]:
                    matching = False
                    break

            if matching:
                return_string += ref_word[i]
            else:
                return return_string
        return return_string

