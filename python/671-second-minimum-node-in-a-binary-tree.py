# Efficient first try solution:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

inf = 2147483647 + 1


class Solution(object):
    def search(self, root, initial):
        if root.left is None:
            return root.val if root.val != initial else inf
        else:
            return min(self.search(root.left, initial), self.search(root.right, initial))

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return_val = self.search(root, root.val)
        return return_val if return_val != inf else -1
