package main

/*
 * @lc app=leetcode.cn id=508 lang=golang
 *
 * [508] 出现次数最多的子树元素和
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start

func findFrequentTreeSum(root *TreeNode) []int {
	cache := make(map[int]int)
	res := make([]int, 0)

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}
		sumNode := node.Val + dfs(node.Left) + dfs(node.Right)
		cache[sumNode] += 1
		return sumNode
	}
	dfs(root)
	maxCount := 0
	for _, count := range cache {
		if count > maxCount {
			maxCount = count
		}
	}
	for sumNode, count := range cache {
		if count == maxCount {
			res = append(res, sumNode)
		}
	}
	return res
}

// @lc code=end
