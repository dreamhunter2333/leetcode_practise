#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        for index in range(2, n):
            s_last = 1 if s[-1] == 2 else 2
            if s[index] == 1:
                s.append(s_last)
            else:
                s.extend([s_last, s_last])
        return s[:n].count(1)


# @lc code=end
print(Solution().magicalString(5))
