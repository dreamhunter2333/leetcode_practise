package main

import "fmt"

/*
 * @lc app=leetcode.cn id=944 lang=golang
 *
 * [944] 删列造序
 */

// @lc code=start
func minDeletionSize(strs []string) int {
	res := 0
	n := len(strs[0])
	m := len(strs)
	for i := 0; i < n; i++ {
		for j := 1; j < m; j++ {
			if strs[j][i] >= strs[j-1][i] {
				continue
			}
			res++
			break
		}
	}
	return res
}

// @lc code=end
func main() {
	fmt.Println(minDeletionSize([]string{"zyx", "wvu", "tsr"}))
}
