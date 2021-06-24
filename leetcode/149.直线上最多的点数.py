#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        n = len(points)
        for x in range(n):
            for y in range(x+1, n):
                cnt = 2
                delta_x1 = points[y][0] - points[x][0]
                delta_y1 = points[y][1] - points[x][1]
                for z in range(y+1, n):
                    delta_x2 = points[z][0] - points[y][0]
                    delta_y2 = points[z][1] - points[y][1]
                    if delta_x1 * delta_y2 == delta_x2 * delta_y1:
                        cnt += 1
                res = max(res, cnt)
        return res

# @lc code=end
