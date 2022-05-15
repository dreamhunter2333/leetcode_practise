package main

import (
	"fmt"
	"math"
)

/*
 * @lc app=leetcode.cn id=812 lang=golang
 *
 * [812] 最大三角形面积
 */

// @lc code=start
func largestTriangleArea(points [][]int) float64 {
	res := 0.0
	n := len(points)
	for i := 0; i < n-2; i++ {
		for j := 1; j < n-1; j++ {
			for k := 2; k < n; k++ {
				x1, y1 := points[i][0], points[i][1]
				x2, y2 := points[j][0], points[j][1]
				x3, y3 := points[k][0], points[k][1]
				cur := math.Abs(float64(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2)) / 2
				res = math.Max(res, cur)
			}
		}
	}
	return res
}

// @lc code=end
func main() {
	fmt.Println(largestTriangleArea([][]int{{0, 0}, {0, 1}, {1, 0}, {0, 2}, {2, 0}}))
}
