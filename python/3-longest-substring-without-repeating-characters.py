# Brute force O(n^2) time-complexity method, 6228 ms, faster than 5.02%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_str = 0
        
        for i in range(len(s)):
            sub_set = set()
            counter = 0
            for j in range(i, len(s)):
                if s[j] in sub_set:
                    break
                else:
                    counter += 1
                    sub_set.add(s[j])
            longest_str = max(longest_str, counter)
        
            
        return longest_str

# Sliding window approach, O(n) time-complexity, O(1) space-complexity, 300ms, 27%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_ind = 0
        right_ind = 1
        longest = 0
        
        def isUnique(string):
            return True if len(string) - len(set(string)) == 0 else False
        
        while right_ind <= len(s):
            # Substring check:
            if isUnique(s[left_ind:right_ind]):
                longest = max(longest, right_ind - left_ind)
                right_ind += 1
            else:
                left_ind += 1
                
        return longest
            
# Sliding window approach with sets, O(n) time-complexity, O(1) space-complexity, 76 ms, faster than 38.39%
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_ind = 0
        right_ind = 0
        longest = 0
        
        char_set = set()
        
        
        while right_ind < len(s):
            if s[right_ind] in char_set:
                char_set.remove(s[left_ind])
                left_ind += 1
            else:
                char_set.add(s[right_ind])
                right_ind += 1
                longest = max(longest, right_ind - left_ind)
            
        return longest
            