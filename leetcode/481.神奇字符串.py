#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#
# https://leetcode-cn.com/problems/magical-string/description/
#
# algorithms
# Medium (48.30%)
# Likes:    23
# Dislikes: 0
# Total Accepted:    1.3K
# Total Submissions: 2.7K
# Testcase Example:  '1'
#
# 神奇的字符串 S 只包含 '1' 和 '2'，并遵守以下规则：
#
# 字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。
#
# 字符串 S 的前几个元素如下：S = “1221121221221121122 ......”
#
# 如果我们将 S 中连续的 1 和 2 进行分组，它将变成：
#
# 1 22 11 2 1 22 1 22 11 2 11 22 ......
#
# 并且每个组中 '1' 或 '2' 的出现次数分别是：
#
# 1 2 2 1 1 2 1 2 2 1 2 2 ......
#
# 你可以看到上面的出现次数就是 S 本身。
#
# 给定一个整数 N 作为输入，返回神奇字符串 S 中前 N 个数字中的 '1' 的数目。
#
# 注意：N 不会超过 100,000。
#
# 示例：
#
# 输入：6
# 输出：3
# 解释：神奇字符串 S 的前 6 个元素是 “12211”，它包含三个 1，因此返回 3。
#
#
#
#
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2 , 2]
        for index in range(2, n):
            s_last = 1 if s[-1] == 2 else 2
            if s[index] == 1:
                s.append(s_last)
            else:
                s.extend([s_last, s_last])
        return s[:n].count(1)


if __name__ == "__main__":
    print(Solution().magicalString(5))
# @lc code=end
