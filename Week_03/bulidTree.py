# 105. 从前序与中序遍历序列构造二叉树
# 根据一棵树的前序遍历与中序遍历构造二叉树。注意：你可以假设树中没有重复的元素。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 充分理解前序遍历和中序遍历的特点，前序遍历的根节点，左右子树位置，对应中序遍历的位置。
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorderIndex = {number: i for i, number in enumerate(inorder)}
        length = len(preorder)
        def buildingTree(preleft, preright, inleft, inright):
            if preleft > preright: return
            preroot = preleft
            inroot = inorderIndex[preorder[preroot]]
            root = TreeNode(preorder[preroot])
            leftSubTreesize = inroot - inleft
            root.left = buildingTree(preleft + 1, preleft + leftSubTreesize, inleft, inroot - 1)
            root.right = buildingTree(preleft + leftSubTreesize + 1, preright, inroot + 1, inright)
            return root
        return buildingTree(0, length - 1, 0, length - 1)
