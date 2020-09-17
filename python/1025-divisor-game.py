# Dynamic programming solution, O(n) time-complexity, O(n) space-complexity
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        P = [False for i in range(N + 1)]
        
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and P[i - j] == False:
                    P[i] = True
        return P[N]

