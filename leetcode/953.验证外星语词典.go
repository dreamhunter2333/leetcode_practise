package main

/*
 * @lc app=leetcode.cn id=953 lang=golang
 *
 * [953] 验证外星语词典
 */

// @lc code=start
import (
	"fmt"
	"reflect"
	"sort"
)

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

type byAlien struct {
	s        []string
	orderMap map[byte]int
}

func (b byAlien) Len() int {
	return len(b.s)
}
func (b byAlien) Swap(i, j int) {
	b.s[i], b.s[j] = b.s[j], b.s[i]
}

func (b byAlien) Less(i, j int) bool {
	for k := 0; k < Min(len(b.s[i]), len(b.s[j])); k++ {
		first := b.orderMap[b.s[i][k]]
		second := b.orderMap[b.s[j][k]]
		if first != second {
			return first < second
		}
	}
	return len(b.s[i]) < len(b.s[j])
}

func isAlienSorted(words []string, order string) bool {
	orderMap := make(map[byte]int)
	for i := 0; i < len(order); i++ {
		orderMap[order[i]] = i
	}
	newWords := make([]string, len(words))
	copy(newWords, words)
	sort.Sort(byAlien{newWords, orderMap})
	return reflect.DeepEqual(words, newWords)
}

// @lc code=end
func main() {
	fmt.Println(isAlienSorted(
		[]string{"apple", "app"}, "abcdefghijklmnopqrstuvwxyz"))
	fmt.Println(isAlienSorted(
		[]string{"hello", "leetcode"}, "hlabcdefgijkmnopqrstuvwxyz"))
	fmt.Println(isAlienSorted(
		[]string{"word", "world", "row"}, "worldabcefghijkmnpqstuvxyz"))
}
