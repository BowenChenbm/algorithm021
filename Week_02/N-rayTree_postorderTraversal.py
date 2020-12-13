# 590. N叉树的后序遍历
# 给定一个 N 叉树，返回其节点值的后序遍历。
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        def postorder(root):
            if root:
                for i in root.children:
                    postorder(i)
                result.append(root.val)
        postorder(root)
        return result
