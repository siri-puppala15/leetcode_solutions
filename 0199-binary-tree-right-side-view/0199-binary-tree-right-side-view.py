# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        ans = []
        s = [-1]
        def rec(root, dep):
            if root is None:
                return
            if dep > s[0]:
                ans.append(root.val)
                s[0] = dep
            rec(root.right, dep + 1)
            rec(root.left, dep + 1)
        rec(root, 0)
        return ans