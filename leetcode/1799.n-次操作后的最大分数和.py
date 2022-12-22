#
# @lc app=leetcode.cn id=1799 lang=python3
#
# [1799] N 次操作后的最大分数和
#
from typing import List


# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        size = 1 << n
        dp = [0] * size

        def gcd(a: int, b: int) -> int:
            if a % b == 0:
                return b
            return gcd(b, a % b)

        gcd_map = {
            i: {
                j: gcd(nums[i], nums[j])
                for j in range(i+1, n)
            }
            for i in range(n)
        }

        for bit in range(1, size):
            bit_count = bit.bit_count()
            if bit_count % 2:
                continue
            for i in range(n):
                if not ((bit >> i) & 1):
                    continue
                for j in range(i+1, n):
                    if not ((bit >> j) & 1):
                        continue
                    dp[bit] = max(
                        dp[bit],
                        dp[
                            bit ^ (1 << i) ^ (1 << j)
                        ] + int(
                            bit_count / 2 * gcd_map[i][j]
                        )
                    )
        return dp[-1]


# @lc code=end
print(Solution().maxScore([1, 2, 3, 4, 5, 6]))
