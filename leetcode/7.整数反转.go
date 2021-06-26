package main

import (
	"fmt"
	"math"
)

/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] 整数反转
 */

// @lc code=start
func reverse(x int) int {
	res := 0
	for x != 0 {
		if res < math.MinInt32/10 || res > math.MaxInt32/10 {
			return 0
		}
		temp := x % 10
		x = x / 10
		res = res*10 + temp
	}
	return res
}

func main() {
	fmt.Println(reverse(1234))
}

// @lc code=end
