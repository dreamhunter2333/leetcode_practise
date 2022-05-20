package main

import "fmt"

/*
 * @lc app=leetcode.cn id=961 lang=golang
 *
 * [961] 在长度 2N 的数组中找出重复 N 次的元素
 */

// @lc code=start
func repeatedNTimes(nums []int) int {
	cacheSet := make(map[int]bool)
	for _, num := range nums {
		if _, ok := cacheSet[num]; ok {
			return num
		}
		cacheSet[num] = true
	}
	return 0
}

// @lc code=end
func main() {
	fmt.Println(repeatedNTimes([]int{1, 2, 3, 3}))
	fmt.Println(repeatedNTimes([]int{2, 1, 2, 5, 3, 2}))
	fmt.Println(repeatedNTimes([]int{5, 1, 5, 2, 5, 3, 5, 4}))
}
