#
# @lc app=leetcode.cn id=1186 lang=python3
#
# [1186] 删除一次得到子数组最大和
#
from typing import List


# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = arr[0]
        dp[1][0] = float("-inf")
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], 0) + arr[i]
            dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])
        return max(max(dp_arr) for dp_arr in dp)


# @lc code=end
print(Solution().maximumSum([1, -2, 0, 3]))
print(Solution().maximumSum([1, -2, -2, 3]))
print(Solution().maximumSum([-1, -1, -1, -1]))
