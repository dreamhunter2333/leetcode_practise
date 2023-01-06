#
# @lc app=leetcode.cn id=2180 lang=python3
#
# [2180] 统计各位数字之和为偶数的整数个数
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num+1):
            sum_i = 0
            while i:
                sum_i += i % 10
                i = i // 10
            if sum_i % 2 == 0:
                res += 1
        return res


# @lc code=end
print(Solution().countEven(4))
print(Solution().countEven(30))
