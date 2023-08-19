#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List


# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[i+2] + nums[i+3] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                p = j + 1
                q = n - 1
                while p < q:
                    sum_nums = nums[i] + nums[j] + nums[p] + nums[q]
                    if sum_nums == target:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1
                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1
                        p += 1
                        q -= 1
                    elif sum_nums > target:
                        q -= 1
                    else:
                        p += 1
        return res


# @lc code=end
print(Solution().fourSum(
    [1, 0, -1, 0, -2, 2],
    target=0
))
print(Solution().fourSum(
    [2, 2, 2, 2, 2],
    target=8
))
