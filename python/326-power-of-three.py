class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 3:
            if n == 3:
                return True
            if n % 3 != 0:
                return False
            n = n // 3
        return True if n == 1 else False
        
        
        