# First attempt 65.32%

class Solution(object):
    def calPoints(self, s):
        """
        :type ops: List[str]
        :rtype: int
        """
        round_dict = {}
        total = 0
        round_index = 1
        i = 0
        while i < len(s):
            if s[i] == "C":
                total -= round_dict.pop(round_index)
                round_index -= 1
            elif s[i] == "D":
                round_index += 1
                round_dict[round_index] = round_dict[round_index - 1] * 2
                total += round_dict[round_index]
            elif s[i] == "+":
                round_index += 1
                round_dict[round_index] = round_dict[round_index - 2] + round_dict[round_index - 1]
                total += round_dict[round_index]
            else:
                round_index += 1
                round_dict[round_index] = int(s[i])
                total += round_dict[round_index]
            i += 1
        return total