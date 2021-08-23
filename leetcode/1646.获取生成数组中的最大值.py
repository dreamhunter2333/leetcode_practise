#
# @lc app=leetcode.cn id=1646 lang=python3
#
# [1646] 获取生成数组中的最大值
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 1:
            return 0
        nums = [0, 1] + [0] * (n - 1)
        for index in range(2, n + 1):
            i = index // 2
            j = index % 2
            nums[index] = (nums[i] + nums[i + j]) if j else nums[i]
        return max(nums)

# @lc code=end
