# First pass solution: 80ms 14.48%
'''
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        character_count = {}
        for char in A[0]:
            if character_count.get(char) is None:
                character_count[char] = 1
            else:
                character_count[char] += 1


        for i in range(1, len(A)):
            current_dict = {}
            for j in range(len(A[i])):
                if character_count.get(A[i][j]) is not None:
                    if current_dict.get(A[i][j]) is not None:
                        current_dict[A[i][j]] += 1
                    else:
                        current_dict[A[i][j]] = 1
            for key in character_count.keys():
                if current_dict.get(key) is not None:
                    character_count[key] = min(character_count[key], current_dict[key])
                else:
                    character_count[key] = 0

        return_list = []
        for key in character_count.keys():
            for i in range(character_count[key]):
                return_list.append(key)

        return return_list
'''

# Most efficient solution using python sets and the reduce function:
from functools import reduce
from operator import add


class Solution:
    def commonChars(self, A):
        unique_chars = set(A[0])

        common_char_occ = [[char] * min((string.count(char) for string in A)) for char in unique_chars]

        result = reduce(add, common_char_occ)

        return result