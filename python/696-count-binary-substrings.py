'''
# Brute force method:
class Solution(object):
    def count(self, s, i):
        depth = 1
        total = 0
        reached_terminator = False
        terminator = int(not int(s[i]))
        terminator_index = -1
        while i + 1 < len(s):
            if int(s[i+1]) == terminator:
                depth -= 1
                total += 1
                if not reached_terminator:
                    reached_terminator = True
                    terminator_index = i + 1
            else:
                if reached_terminator:
                    break
                depth += 1
            if depth == 0:
                break
            i += 1
        return total, terminator_index

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        terminator_index = 0
        while terminator_index != -1:
            contribution, terminator_index = self.count(s, terminator_index)
            total += contribution
        return total
'''

# Elegant method:
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev_count = 0
        cur_count = 0
        cur_char = int(s[0])
        total = 0
        for i in range(len(s)):
            if int(s[i]) != cur_char:
                total += min(prev_count, cur_count)
                prev_count = cur_count
                cur_count = 1
                cur_char = int(s[i])
            else:
                cur_count += 1
            if i == len(s) - 1:
                total += min(prev_count, cur_count)
        return total
