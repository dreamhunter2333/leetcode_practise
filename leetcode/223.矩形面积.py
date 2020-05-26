#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (A-C)*(B-D) + (E-G)*(F-H) - max(
                min(C,G)-max(A,E), 0
            ) * max(
                min(D,H)-max(B,F), 0
            )

if __name__ == "__main__":
    print(Solution().computeArea(0, 0, 0, 0, -1, -1, 1, 1))
# @lc code=end

