#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
from collections import defaultdict
from typing import List


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x_obstacles = defaultdict(list)
        y_obstacles = defaultdict(list)
        for x, y in obstacles:
            x_obstacles[x].append(y)
            y_obstacles[y].append(x)

        res = 0
        direction = 0
        pos_x, pos_y = 0, 0
        for command in commands:

            if command == -1:
                direction += 1
                continue
            if command == -2:
                direction += 3
                continue
            direction = direction % 4
            if direction == 0:
                ob_ys = [
                    ob_y for ob_y in x_obstacles[pos_x]
                    if ob_y > pos_y
                ]
                pos_y = min(
                    pos_y + command, min(ob_ys) - 1
                ) if ob_ys else (pos_y + command)
            elif direction == 1:
                ob_xs = [
                    ob_x for ob_x in y_obstacles[pos_y]
                    if ob_x > pos_x
                ]
                pos_x = min(
                    pos_x + command, min(ob_xs) - 1
                ) if ob_xs else (pos_x + command)
            elif direction == 2:
                ob_ys = [
                    ob_y for ob_y in x_obstacles[pos_x]
                    if ob_y < pos_y
                ]
                pos_y = max(
                    pos_y - command, max(ob_ys) + 1
                ) if ob_ys else (pos_y - command)
            elif direction == 3:
                ob_xs = [
                    ob_x for ob_x in y_obstacles[pos_y]
                    if ob_x < pos_x
                ]
                pos_x = max(
                    pos_x - command, max(ob_xs) + 1
                ) if ob_xs else (pos_x - command)

            res = max(res, pos_x ** 2 + pos_y ** 2)

        return res


# @lc code=end
print(Solution().robotSim(
    commands=[7, -2, -2, 7, 5], obstacles=[[-3, 2], [-2, 1], [0, 1], [-2, 4], [-1, 0], [-2, -3], [0, -3], [4, 4], [-3, 3], [2, 2]]
))
print(Solution().robotSim(
    commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]]
))
