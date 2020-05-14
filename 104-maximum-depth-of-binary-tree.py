# First pass solution: 36ms, 30.43%
'''
class Solution(object):
    def depthSearch(self, root):

        if root.left is None and root.right is None:
            return 0
        elif root.right is None:
            return 1 + max(0, self.depthSearch(root.left))
        elif root.left is None:
            return 1 + max(0, self.depthSearch(root.right))
        else:
            return 1 + max(max(0, self.depthSearch(root.right)), self.depthSearch(root.left))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        return self.depthSearch(root) + 1
'''

# Optimal solution: 16ms, 99%
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)