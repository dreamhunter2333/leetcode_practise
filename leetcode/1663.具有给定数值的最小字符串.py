#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        count_z = (k - n) // 25
        offset = (k - n) % 25
        res = ["z"] * count_z
        if offset:
            res = [chr(ord("a") + offset)] + res
        res = ["a"] * (n - len(res)) + res
        return "".join(res)


# @lc code=end
print(Solution().getSmallestString(n=3, k=27))
print(Solution().getSmallestString(n=5, k=73))
print(Solution().getSmallestString(n=5, k=130))
