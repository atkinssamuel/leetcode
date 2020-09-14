# log(n) time-complexity, 20 ms, faster than 65.25%
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_five_multiples = 0
        
        while n >= 5:
            num_five_multiples += n // 5
            n = n // 5
        
        return num_five_multiples
            