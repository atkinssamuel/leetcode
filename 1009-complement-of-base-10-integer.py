# First pass solution: 16ms 71.87%
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        index = 0

        while True:
            rem = N % 2
            res += int(int(not rem) * 2 ** index)
            N = N // 2
            index += 1
            if N == 0:
                return res

