#
# @lc app=leetcode.cn id=1758 lang=python3
#
# [1758] 生成交替二进制字符串的最少操作数
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        bit_map = {"1": "0", "0": "1"}
        bit = "0"
        for c in s:
            if bit == c:
                count += 1
            bit = bit_map[bit]
        return min(count, len(s) - count)


# @lc code=end
print(Solution().minOperations("10"))
