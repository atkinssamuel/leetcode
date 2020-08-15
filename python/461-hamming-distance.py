# First pass: 56.55%, 20ms
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x == y:
            return 0

        count = 0

        while True:
            if x == 0 and y == 0:
                return count
            x_rem = x % 2
            y_rem = y % 2

            if x_rem != y_rem:
                count += 1

            x = x // 2
            y = y // 2