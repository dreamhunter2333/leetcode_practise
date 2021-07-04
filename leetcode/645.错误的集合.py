#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        delta = n * (n + 1) // 2 - sum(nums)

        while i < n:
            if nums[i] == i + 1:
                i += 1
                continue
            j = nums[i] - 1
            if nums[j] == nums[i]:
                return [j+1, j + 1 + delta]
            nums[i], nums[j] = nums[j], nums[i]

        return [-1, -1]

# @lc code=end
