package main

import "math/rand"

/*
 * @lc app=leetcode.cn id=710 lang=golang
 *
 * [710] 黑名单中的随机数
 */

// @lc code=start
type Solution struct {
	bound int
	data  map[int]int
}

func Constructor(n int, blacklist []int) Solution {
	m := len(blacklist)
	bound := n - m
	start := n - m
	blackMap := map[int]bool{}
	for _, b := range blacklist {
		if b >= bound {
			blackMap[b] = true
		}
	}

	data := make(map[int]int, m-len(blackMap))
	for _, b := range blacklist {
		if b < bound {
			for blackMap[start] {
				start++
			}
			data[b] = start
			start++
		}
	}
	return Solution{bound, data}
}

func (this *Solution) Pick() int {
	res := rand.Intn(this.bound)
	if this.data[res] > 0 {
		return this.data[res]
	}
	return res
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(n, blacklist);
 * param_1 := obj.Pick();
 */
// @lc code=end
