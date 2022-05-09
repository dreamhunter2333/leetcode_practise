package main

/*
 * @lc app=leetcode.cn id=942 lang=golang
 *
 * [942] 增减字符串匹配
 */

// @lc code=start
func diStringMatch(s string) []int {
	res := make([]int, 0)
	start := 0
	end := len(s)
	for _, c := range s {
		if c == 'I' {
			res = append(res, start)
			start++
		} else {
			res = append(res, end)
			end--
		}
	}
	res = append(res, end)
	return res
}

// func main() {
// 	fmt.Println(diStringMatch("IDID"))
// }
// @lc code=end
