package main

import "fmt"

/*
 * @lc app=leetcode.cn id=890 lang=golang
 *
 * [890] 查找和替换模式
 */

// @lc code=start
func findAndReplacePattern(words []string, pattern string) []string {
	res := make([]string, 0)
	for _, word := range words {
		if !check(word, pattern) {
			continue
		}
		res = append(res, word)
	}
	return res
}

func check(word string, pattern string) bool {
	cache := make(map[byte]byte)
	cache2 := make(map[byte]byte)
	for i, _ := range pattern {
		if value, ok := cache[pattern[i]]; ok && value != word[i] {
			return false
		}
		if value, ok := cache2[word[i]]; ok && value != pattern[i] {
			return false
		}
		cache[pattern[i]] = word[i]
		cache2[word[i]] = pattern[i]
	}
	return true
}

// @lc code=end
func main() {
	fmt.Println(findAndReplacePattern([]string{"abc", "deq", "mee", "aqq", "dkd", "ccc"}, "abb"))
}
