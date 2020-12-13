# 589. N叉树的前序遍历
# 给定一个 N 叉树，返回其节点值的前序遍历。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def preorder(root):
            if root:
                result.append(root.val)
                for i in root.children:
                    preorder(i)
        preorder(root)
        return result

