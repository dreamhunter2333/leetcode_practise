package main

import (
	"fmt"
	"sort"
)

/*
 * @lc app=leetcode.cn id=462 lang=golang
 *
 * [462] 最少移动次数使数组元素相等 II
 */

// @lc code=start
func minMoves2(nums []int) int {
	sort.Ints(nums)
	target := nums[len(nums)/2]
	res := 0
	for _, num := range nums {
		res += Abs(target - num)
	}
	return res
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// @lc code=end
func main() {
	fmt.Println(minMoves2([]int{1, 2, 3}))
	fmt.Println(minMoves2([]int{1, 10, 2, 9}))
}
