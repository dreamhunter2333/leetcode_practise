#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

# @lc code=start
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        mid = len(buildings) // 2
        left = self.getSkyline(buildings[:mid])
        right = self.getSkyline(buildings[mid:])
        return self.merge(left, right)

    # 两个合并
    def merge(self, left, right):
        # 记录目前左右建筑物的高度
        lheight = rheight = 0
        # 位置
        l = r = 0
        # 输出结果
        res = []
        while l < len(left) and r < len(right):
            if left[l][0] < right[r][0]:
                # current point
                cp = [left[l][0], max(left[l][1], rheight)]
                lheight = left[l][1]
                l += 1
            elif left[l][0] > right[r][0]:
                cp = [right[r][0], max(right[r][1], lheight)]
                rheight = right[r][1]
                r += 1
            # 相等情况
            else:
                cp = [left[l][0], max(left[l][1], right[r][1])]
                lheight = left[l][1]
                rheight = right[r][1]
                l += 1
                r += 1
            # 和前面高度比较，不一样才加入
            if len(res) == 0 or res[-1][1] != cp[1]:
                res.append(cp)
        # 剩余部分添加进去
        res.extend(left[l:] or right[r:])
        return res


print(Solution().getSkyline(
    [[1, 20, 1], [1, 21, 2], [1, 22, 3]]
))
# @lc code=end
