package main

/*
 * @lc app=leetcode.cn id=1022 lang=golang
 *
 * [1022] 从根到叶的二进制数之和
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start
func sumRootToLeaf(root *TreeNode) int {
	return dfs(root, 0, 0)
}

func dfs(node *TreeNode, num int, res int) int {
	if node == nil {
		return res
	}
	num = num*2 + node.Val
	if node.Left == nil && node.Right == nil {
		res += num
		return res
	}
	res = dfs(node.Left, num, res)
	res = dfs(node.Right, num, res)
	return res
}

// @lc code=end
