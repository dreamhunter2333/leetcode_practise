#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from typing import List


# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        cache_set = set()
        i = 0
        n = len(popped)
        for num in pushed:
            stack.append(num)
            cache_set.add(num)
            while i < n and popped[i] in cache_set:
                if popped[i] != stack[-1]:
                    return False
                stack.pop()
                i += 1
        return True


# @lc code=end
print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]
))
print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]
))
