package main

/*
 * @lc app=leetcode.cn id=713 lang=golang
 *
 * [713] 乘积小于K的子数组
 */

// @lc code=start
func numSubarrayProductLessThanK(nums []int, k int) int {
	n := len(nums)
	var multiSum int = 1
	res := 0
	left := 0
	right := 0

	for right < n {
		multiSum *= nums[right]
		for left <= right && multiSum >= k {
			multiSum = multiSum / nums[left]
			left += 1
		}
		res += right - left + 1
		right += 1
	}
	return res
}

// func main() {
// 	fmt.Println(numSubarrayProductLessThanK([]int{10, 5, 2, 6}, 100))
// }
// @lc code=end
