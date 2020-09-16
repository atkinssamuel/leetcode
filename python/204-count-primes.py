# Brute force, O(n^2) time-complexity, O(1) space-complexity, too slow
# NOTE: Don't have to check for factors greater than sqrt(n)
def isPrime(n):
    upper_bound = int(math.floor(sqrt(n)))
    for i in range(2, upper_bound+1):
        # print(n)
        # print("{}".format(i) +"\n")
        if n % i == 0:
            return 0
    return 1
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0
        for i in range(2, n):
            counter += isPrime(i)
        
        return counter

# Sieve of Eratosthenes, O(n * log(n)), 768 ms, faster than 62.35%
# NOTE: Don't have to check for factors greater than sqrt(n)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        
        
        prime_list = n * [True]
        
        prime_list[0] = False
        prime_list[1] = False
        
        for i in range(2, len(prime_list)):
            if prime_list[i] == False:
                continue
            for j in range(2 * i, len(prime_list), i):
                prime_list[j] = False
            
        
        return sum(prime_list)
    
# Sieve of Eratosthenes, O(n * log(n))
