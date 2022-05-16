package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
 * 面试题 04.06
 */
func inorderSuccessor(root *TreeNode, p *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	var res *TreeNode
	cur := root
	for cur != nil {
		if cur.Val > p.Val {
			res = cur
			cur = cur.Left
		} else {
			cur = cur.Right
		}
	}
	return res
}
