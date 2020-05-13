# First pass solution: 452ms 6.63%
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)

        s_values_list = list(set(ord(element) for element in s))
        s_values_list.sort()
        s_values_list_reverse = list(s_values_list)
        s_values_list_reverse.reverse()
        s_values_order = s_values_list + s_values_list_reverse

        return_string = ""

        while len(s) > 0:
            for element in s_values_order:
                for i in range(len(s)):
                    if ord(s[i]) == element:
                        return_string += s.pop(i)
                        break

        return return_string


