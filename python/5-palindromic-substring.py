# Center expand method, O(n^2) time-complexity, O(n) space-complexity, 1904 ms, faster than 42.58%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_ind = 0
        right_ind = 0
        longest = 0
        max_palindrome = ""
        
        if len(s) == 1:
            return s
        
        def find_palindrome(s, p, left_ind, right_ind):
            while right_ind < len(s) and left_ind >= 0:
                if s[left_ind] == s[right_ind]:
                    p = s[left_ind] + p + s[right_ind]
                    left_ind -= 1
                    right_ind += 1
                else:
                    return p
            return p
        
        while right_ind < len(s):
            if left_ind == right_ind:
                p = s[left_ind]
                palindrome_iter = find_palindrome(s, p, left_ind-1, right_ind+1)
                right_ind += 1
            else:
                p = ""
                palindrome_iter = find_palindrome(s, p, left_ind, right_ind)
                left_ind += 1
            
            
            if len(palindrome_iter) > longest:
                max_palindrome = palindrome_iter
                longest = len(max_palindrome)
                
        return max_palindrome