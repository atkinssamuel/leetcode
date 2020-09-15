# Simple 1 counter using string rep of n, 16 ms, faster than 90.10%
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bit_str = str(bin(n))
        
        count = 0
        
        for element in bit_str:
            if element == "1":
                count += 1
                
        return count