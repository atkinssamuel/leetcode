# First pass solution using a stack: 28ms, 20.96%
class Solution(object):
    left_bracket_set = {"(", "[", "{"}
    left_bracket_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    right_bracket_set = {"}", "]", ")"}

    def isValid(self, s):
        bracket_stack = []
        if len(s) == 0:
            return True
        for character in s:
            if character in self.left_bracket_set:
                bracket_stack.append(character)
            else:
                # The current character is a right bracket. We need to check for the corresponding left bracket
                if len(bracket_stack) == 0:
                    return False

                if self.left_bracket_dict[bracket_stack[-1]] == character:
                    bracket_stack.pop()
                else:
                    return False

        if len(bracket_stack) == 0:
            return True
        return False