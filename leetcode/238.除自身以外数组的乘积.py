#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [None] * n
        cache1 = [1] + [None] * (n-1)
        cache2 = [None] * (n-1) + [1]

        for i in range(1, n):
            cache1[i] = cache1[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            cache2[i] = cache2[i+1] * nums[i+1]

        for i in range(n):
            res[i] = cache1[i] * cache2[i]
        return res

# @lc code=end
