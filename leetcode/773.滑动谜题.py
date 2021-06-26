#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        target = [[1, 2, 3], [4, 5, 0]]
        if target == board:
            return 0
        cache = set()

        def move(x, y):
            yield (0, y) if x == 1 else (1, y)
            if y > 0:
                yield (x, y - 1)
            if y < 2:
                yield (x, y + 1)

        def bfs(cur_set, count):
            if not cur_set:
                return -1
            next_set = []
            for cur, x, y in cur_set:
                if str(cur) in cache:
                    continue
                cache.add(str(cur))
                for p, q in move(x, y):
                    next_l = [cur[0][:], cur[1][:]]
                    next_l[p][q], next_l[x][y] = next_l[x][y], next_l[p][q]
                    if next_l == board:
                        return count + 1
                    next_set.append([next_l, p, q])
            return bfs(next_set, count + 1)

        return bfs([[target, 1, 2]], 0)


print(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
# @lc code=end
