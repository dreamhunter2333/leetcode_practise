package main

import "fmt"

/*
 * @lc app=leetcode.cn id=513 lang=golang
 *
 * [513] 找树左下角的值
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start

func findBottomLeftValue(root *TreeNode) int {
	nodeList := make([]*TreeNode, 0)
	nodeList = append(nodeList, root)
	var res *TreeNode
	for len(nodeList) > 0 {
		res = nodeList[0]
		newNodeList := make([]*TreeNode, 0)
		for _, node := range nodeList {
			if node.Left != nil {
				newNodeList = append(newNodeList, node.Left)
			}
			if node.Right != nil {
				newNodeList = append(newNodeList, node.Right)
			}
		}
		nodeList = newNodeList
	}
	return res.Val
}

// @lc code=end
func main() {
	fmt.Println(findBottomLeftValue(&TreeNode{2, &TreeNode{1, nil, nil}, &TreeNode{3, nil, nil}}))
}
