#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode-cn.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (59.39%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    23.1K
# Total Submissions: 37.7K
# Testcase Example:  '"abc"'
#
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
# 示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
# 示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
# 注意:
#
#
# 输入的字符串长度不会超过1000。
#
#
#

# @lc code=start


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        TODO: 解法
        https://leetcode.com/problems/palindromic-substrings/discuss/392119
        """
        L = len(s)
        result = 0
        for i in range(L):
            for a, b in [(i, i), (i, i+1)]:
                while a >= 0 and b < L and s[a] == s[b]:
                    a -= 1
                    b += 1
                result += (b-a)//2
        return result


if __name__ == "__main__":
    print(Solution().countSubstrings('aaa'))
# @lc code=end
