# First pass with log checking: 20ms 51.38%
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        if log(num, 2).is_integer():
            return int(log(num, 2)) + 1
        elif (log(num - 1, 2)).is_integer():
            return int(log(num - 1, 2)) + 2

        total = 0
        while num != 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
            total += 1
        return total