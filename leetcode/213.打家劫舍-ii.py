#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[1], nums[0])

        dp1 = [0] * (n - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[1], nums[0])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        dp2 = [0] * (n - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[2], nums[1])
        for i in range(2, n-1):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1])

        return max(dp1[-1], dp2[-1])

# @lc code=end
