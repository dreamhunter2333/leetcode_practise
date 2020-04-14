#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] 子串能表示从 1 到 N 数字的二进制串
#
# https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (56.08%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    1.7K
# Total Submissions: 3K
# Testcase Example:  '"0110"\n3'
#
# 给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S
# 的子串，就返回 true，否则返回 false。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "0110", N = 3
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：S = "0110", N = 4
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= S.length <= 1000
# 1 <= N <= 10^9
# 
# 
#

# @lc code=start


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(N):
            if str(bin(i+1))[2:] in S:
                continue
            return False
        return True


if __name__ == "__main__":
    print(Solution().queryString("0110", 3))

# @lc code=end

