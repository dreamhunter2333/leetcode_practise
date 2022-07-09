#
# @lc app=leetcode.cn id=873 lang=python3
#
# [873] 最长的斐波那契子序列的长度
#

from typing import List


# @lc code=start
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        cahce_map = {
            arr[i]: i
            for i in range(n)
        }

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if arr[i] - arr[j] >= arr[j]:
                    break
                if arr[i] - arr[j] not in cahce_map:
                    continue
                k = cahce_map[arr[i] - arr[j]]
                dp[i][j] = max(dp[j][k] + 1, 3)
                res = max(res, dp[i][j])

        return res


# @lc code=end
print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
print(Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
