package main

/*
 * @lc app=leetcode.cn id=933 lang=golang
 *
 * [933] 最近的请求次数
 */

// @lc code=start
type RecentCounter struct {
	count int
	data  []int
}

func Constructor() RecentCounter {
	return RecentCounter{0, make([]int, 0)}
}

func (this *RecentCounter) Ping(t int) int {
	for i := this.count; i < len(this.data); i++ {
		if t-this.data[i] <= 3000 {
			break
		}
		this.count += 1
	}
	this.data = append(this.data, t)
	return len(this.data) - this.count
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
// func main() {
// 	obj := Constructor()
// 	fmt.Println(obj.Ping(1), obj.Ping(100), obj.Ping(3001), obj.Ping(3002))
// }
// @lc code=end
