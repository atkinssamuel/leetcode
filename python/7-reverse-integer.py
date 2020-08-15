# Initial solution:
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res_list = []
        break_flag = False

        # Setting negative flag to reverse number later if needed
        negative_flag = 1
        if x < 0:
            x = x * -1
            negative_flag = -1

        # Checking if number is 1 digit
        if x//10 == 0:
            return x * negative_flag

        # Main loop for list creation
        while True:
            res_list.append(x%10)
            x = x//10
            if x//10 == 0:
                if break_flag == True:
                    break
                break_flag = True

        # Forming the return number
        result = 0
        for i in range(len(res_list), 0, -1):
            result += 10**(i-1) * res_list[len(res_list) - i]
        if negative_flag == -1:
            if result * negative_flag < -2**31:
                return 0
        else:
            if result * negative_flag > 2**31 - 1:
                return 0
        return result*negative_flag
'''

# One pass elegant solution:
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Setting negative flag to reverse number later if needed
        negative_flag = 1 if x >= 0 else -1
        x *= negative_flag

        result = 0
        while True:
            result += x % 10
            if x // 10 == 0:
                break
            x = x // 10
            result *= 10

        # Checking for overflow:
        if negative_flag == -1:
            if result * negative_flag < -2 ** 31:
                return 0
        else:
            if result * negative_flag > 2 ** 31 - 1:
                return 0

        return result * negative_flag