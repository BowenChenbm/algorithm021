# 94. 二叉树的中序遍历
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
# python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        result = []
        inorder(root)
        return result

