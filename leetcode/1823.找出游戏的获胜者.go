package main

/*
 * @lc app=leetcode.cn id=1823 lang=golang
 *
 * [1823] 找出游戏的获胜者
 */

// @lc code=start
func findTheWinner(n int, k int) int {
	data := make([]int, n)
	for i := range data {
		data[i] = i + 1
	}
	j := 0
	allSum := n
	for len(data) > 1 {
		j = (j+k%allSum)%allSum - 1
		if j == -1 {
			j = allSum - 1
		}
		data = append(data[:j], data[j+1:]...) // 删除中间1个元素
		allSum -= 1
	}
	return data[0]
}

// func main() {
// 	fmt.Println(findTheWinner(5, 2))
// }
// @lc code=end
