#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in nums_dict and i - nums_dict[num] <= k:
                return True
            nums_dict[num] = i
        return False

# @lc code=end
