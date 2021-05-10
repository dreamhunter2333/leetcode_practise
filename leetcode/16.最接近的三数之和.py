#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        num_len = len(nums)
        cur_target = None

        for index in range(num_len - 2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            num1 = nums[index]
            i = index + 1
            j = num_len - 1
            while i < j:
                num3_sum = num1 + nums[i] + nums[j]
                if num3_sum == target:
                    return target
                if cur_target is None:
                    cur_target = num3_sum
                elif abs(num3_sum - target) < abs(cur_target - target):
                    cur_target = num3_sum
                if num3_sum < target:
                    i += 1
                else:
                    j -= 1

        return cur_target

# @lc code=end
