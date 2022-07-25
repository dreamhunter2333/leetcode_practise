#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if not node.left or not node.right:
                self.res.append(node)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val=val)
        node = self.res[0]
        if not node.left:
            node.left = new_node
        else:
            node.right = new_node
            self.res.pop(0)
        self.res.append(new_node)
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# @lc code=end

# Your CBTInserter object will be instantiated and called as such:
obj = CBTInserter(TreeNode(val=1))
print(obj.insert(2))
print(obj.get_root())
