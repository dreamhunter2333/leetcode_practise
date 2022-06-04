package main

import (
	"fmt"
	"strings"
)

/*
 * @lc app=leetcode.cn id=929 lang=golang
 *
 * [929] 独特的电子邮件地址
 */

// @lc code=start
func numUniqueEmails(emails []string) int {
	cache := make(map[string]bool, 0)
	for _, email := range emails {
		res := strings.Split(email, "@")
		name := res[0]
		domain := res[1]
		name = strings.ReplaceAll(name, ".", "")
		if strings.Contains(name, "+") {
			name = name[:strings.Index(name, "+")]
		}
		cache[name+"@"+domain] = true
	}
	return len(cache)
}

// @lc code=end
func main() {
	fmt.Println(numUniqueEmails([]string{"test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}))
	fmt.Println(numUniqueEmails([]string{"a@leetcode.com", "b@leetcode.com", "c@leetcode.com"}))
}
