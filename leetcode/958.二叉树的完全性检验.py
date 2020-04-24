#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
#
# https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (45.26%)
# Likes:    38
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 8.9K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# 给定一个二叉树，确定它是否是一个完全二叉树。
# 
# 百度百科中对完全二叉树的定义如下：
# 
# 若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h
# 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2^h 个节点。）
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中将会有 1 到 100 个结点。
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, L = None, R = None):
        self.val = x
        self.left = L
        self.right = R
    
    def __repr__(self):
        return "[Self: {0}]/L: {1}/R: {2}" \
            .format(self.val, self.left.val if self.left else None, self.right.val if self.right else None)

def List2TN(lst, needs = None):
    nit = []
    root = TreeNode(lst[0])
    tnQ = [root]
    i = 1
    if needs and i in needs:
        nit.append(root)
    while i < len(lst):
        cur = tnQ.pop(0)
        if lst[i]!=None:
            cur.left = TreeNode(lst[i])
            tnQ.append(cur.left)
            if needs and i in needs:
                nit.append(cur.left)
        i+=1
        if i >= len(lst):
            break
        if lst[i]!=None:
            cur.right = TreeNode(lst[i])
            tnQ.append(cur.right)
            if needs and i in needs:
                nit.append(cur.right)
        i+=1
    if needs:
        return root, nit
    else:
        return root

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False
        Q = [root]
        
        while Q:
            cur_node = Q.pop(0)
            if not cur_node:
                have_null = True
                continue
            if have_null:
                return False
            Q.append(cur_node.left)
            Q.append(cur_node.right)
            
        return True


if __name__ == "__main__":
    root = List2TN([1,2,3,4,5,None,7])
    print(Solution().isCompleteTree(root))

# @lc code=end

