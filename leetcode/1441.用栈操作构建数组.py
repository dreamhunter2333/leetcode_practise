#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#


from typing import List


# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        pre = 0
        for i in target:
            if i - pre > 1:
                res.extend(
                    ["Push", "Pop"] * (i - pre - 1)
                )
            res.append("Push")
            pre = i
        return res


# @lc code=end
print(Solution().buildArray(target=[1, 3], n=3))
print(Solution().buildArray(target=[1, 2, 3], n=3))
print(Solution().buildArray(target=[2, 3, 4], n=4))
