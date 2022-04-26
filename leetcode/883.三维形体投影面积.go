package main

/*
 * @lc app=leetcode.cn id=883 lang=golang
 *
 * [883] 三维形体投影面积
 */

// @lc code=start
func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func projectionArea(grid [][]int) int {
	res := 0
	n := len(grid)
	maxYZ := make([]int, n, n)
	for x := 0; x < n; x++ {
		maxZ := 0
		for y := 0; y < n; y++ {
			if grid[x][y] == 0 {
				continue
			}
			res += 1
			maxYZ[y] = Max(maxYZ[y], grid[x][y])
			maxZ = Max(maxZ, grid[x][y])
		}
		res += maxZ
	}
	for _, maxZ := range maxYZ {
		res += maxZ
	}
	return res
}

// func main() {
// 	fmt.Println(projectionArea([][]int{
// 		{1, 2},
// 		{3, 4},
// 	}))
// }

// @lc code=end
