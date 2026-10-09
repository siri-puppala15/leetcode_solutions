# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        while root:
            if root.left is None:
                ans.append(root.val)
                root = root.right
            else:
                ln = root.left
                while ln.right and ln.right != root:
                    ln = ln.right
                if ln.right is None:
                    ln.right = root
                    root = root.left
                else:
                    ln.right = None
                    ans.append(root.val)
                    root = root.right
        return ans