#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        num_set = set(str(i) for i in range(10))

        res = 0
        # 是否是负数
        flag = False
        # 是否在找数字前的内容
        find_num = True
        for j in range(len(s)):

            # 处理数字前的逻辑
            if find_num:
                if s[j] in (' '):
                    continue
                elif s[j] == '-' and j < len(s) - 1 and s[j+1] in num_set:
                    flag = True
                    continue
                elif s[j] == '+' and j < len(s) - 1 and s[j+1] in num_set:
                    flag = False
                    continue

            # 开始寻找数字
            if s[j] in num_set:
                res = res * 10 + int(s[j])
                find_num = False
            else:
                # 非数字停止
                break

        # 边界
        return max(-res, -2 ** 31) if flag else min(res, 2 ** 31 - 1)

# @lc code=end
