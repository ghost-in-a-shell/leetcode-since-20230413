class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while q:
            tmp = q
            q = []
            next_level_sum = 0  # 下一层的节点值之和
            for node in tmp:
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val

            # 再次遍历，更新下一层的节点值
            for node in tmp:
                child_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left: node.left.val = next_level_sum - child_sum
                if node.right: node.right.val = next_level_sum - child_sum
        return root