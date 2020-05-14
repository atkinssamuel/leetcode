# First pass solution with dictionary counter: 64ms 18.55%
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        counter_dict = {}


        for i in range(max(len(s), len(t))):
            if i < len(s):
                if counter_dict.get(s[i]) is None:
                    counter_dict[s[i]] = 1
                else:
                    counter_dict[s[i]] += 1

            if i < len(t):
                if counter_dict.get(t[i]) is None:
                    counter_dict[t[i]] = -1
                else:
                    counter_dict[t[i]] -= 1

        for value in counter_dict.values():
            if value != 0:
                return False

        return True

'''

# Sorting method: 44ms 64.07%
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)

        s.sort()
        t.sort()

        if s == t:
            return True
        else:
            return False

