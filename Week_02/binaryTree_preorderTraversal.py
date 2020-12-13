# 144. 二叉树的前序遍历
# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if root:
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)
        result = []
        preorder(root)
        return result
