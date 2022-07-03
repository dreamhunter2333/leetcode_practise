#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
MAX_RES = 2 ** 31


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        nums = list(map(int, str(n)))

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] <= nums[i-1]:
                continue
            max_i = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i-1]:
                    max_i = j
            nums[i-1], nums[max_i] = nums[max_i], nums[i-1]
            nums[i:] = nums[i:][::-1]
            res = int("".join(map(str, nums)))

            if MAX_RES > res:
                return res
            break

        return -1


# @lc code=end
print(Solution().nextGreaterElement(12))
print(Solution().nextGreaterElement(21))
print(Solution().nextGreaterElement(1243))
print(Solution().nextGreaterElement(230241))
print(Solution().nextGreaterElement(2147483476))
