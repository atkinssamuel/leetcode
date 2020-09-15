# Simple reverse the string of bits method, 20 ms, faster than 72.11%
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit_str = str(bin(n))[2:]
        return_val = 0
        zero_string = ""
        for i in range(32 - len(bit_str)):
            zero_string = zero_string + "0"
        bit_str = zero_string + bit_str
        for i in range(len(bit_str)):
            return_val += int(bit_str[i]) * pow(2, i)
            
        return return_val