package main

import (
	"fmt"
	"strings"
)

/*
 * @lc app=leetcode.cn id=1108 lang=golang
 *
 * [1108] IP 地址无效化
 */

// @lc code=start
func defangIPaddr(address string) string {
	return strings.ReplaceAll(address, ".", "[.]")
}

// @lc code=end
func main() {
	fmt.Println(defangIPaddr("1.1.1.1"))
}
