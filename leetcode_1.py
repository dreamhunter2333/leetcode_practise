# -*- coding: utf-8 -*-

"""
1. 两数之和

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        nums_dict ={}
        for index,num in enumerate(nums):
            num2 = target - num
            if nums_dict.get(num2) is not None:
                return [nums_dict.get(num2),index]
            nums_dict[num] = index

if __name__ == "__main__":
    print(Solution().twoSum(nums=[2, 7, 11, 15],target=9))