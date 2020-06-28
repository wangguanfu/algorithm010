class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)  # 这部 获取位置
        root.left = self.buildTree(preorder[1:i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])

        return root
