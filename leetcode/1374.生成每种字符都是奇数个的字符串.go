package main

import "strings"

/*
 * @lc app=leetcode.cn id=1374 lang=golang
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
func generateTheString(n int) string {
	delta := "a"
	if n%2 == 0 {
		delta = "b"
	}
	return strings.Repeat("a", n-1) + delta
}

// @lc code=end
