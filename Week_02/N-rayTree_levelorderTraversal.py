# 429. N 叉树的层序遍历
# 给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
# 输入：root = [1,null,3,2,4,null,5,6]
# 输出：[[1],[3,2,4],[5,6]]
# python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        
        def nodeTraverse(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for chi in node.children:
                nodeTraverse(chi, level+1)
        
        if root != None:
            nodeTraverse(root, 0)

        return result

