# First pass solution: 28ms 84.06%
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output_array = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                output_array.append("FizzBuzz")
            elif i % 3 == 0:
                output_array.append("Fizz")
            elif i % 5 == 0:
                output_array.append("Buzz")
            else:
                output_array.append(str(i))

        return output_array
