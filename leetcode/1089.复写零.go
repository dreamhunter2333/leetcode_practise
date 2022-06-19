package main

/*
 * @lc app=leetcode.cn id=1089 lang=golang
 *
 * [1089] 复写零
 */

// @lc code=start
func duplicateZeros(arr []int) {
	top := 0
	i := -1
	n := len(arr)
	j := n - 1
	for top < n {
		i++
		top++
		if arr[i] == 0 {
			top++
		}
	}
	if top == n+1 {
		arr[j] = 0
		j--
		i--
	}
	for j >= 0 {
		arr[j] = arr[i]
		if arr[i] == 0 {
			arr[j-1] = 0
			j--
		}
		j--
		i--
	}

}

// @lc code=end
