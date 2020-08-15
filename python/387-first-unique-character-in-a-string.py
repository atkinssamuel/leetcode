# My solution:
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_dict = {}
        seen_index_dict = {}
        for i in range(len(s)):
            if seen_dict.get(s[i]) is not None:
                if seen_dict[s[i]] == -1:
                    continue
                seen_index_dict.pop(seen_dict[s[i]])
                seen_dict[s[i]] = -1

            else:
                seen_dict[s[i]] = i
                seen_index_dict[i] = s[i]

        for i in range(len(s)):
            res = seen_index_dict.get(i)
            if res is not None:
                return seen_dict[res]
        return -1
'''

# Elegant second try:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen_dict = {}

        for i in range(len(s)):
            seen_dict[s[i]] = 2 if (seen_dict.get(s[i]) is not None) else 1

        for i in range(len(s)):
            if seen_dict[s[i]] < 2:
                return i
        return -1