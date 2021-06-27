#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        stack = [(1, 0)]
        cache = set()
        n = len(board)
        end = n * n

        def get_index(num):
            p = num % n
            q = num // n
            if p == 0:
                x = n - q
                y = n - 1 if q % 2 else 0
            else:
                x = n - 1 - q
                y = n - p if q % 2 else p - 1
            if x < n and y < n and board[x][y] != -1:
                num = board[x][y]
            return num

        while stack:
            x, count = stack.pop(0)
            if x > end or x in cache:
                continue
            cache.add(x)
            for y in range(x+1, x+7):
                z = get_index(y)
                if z == end:
                    return count + 1
                stack.append((z, count+1))

        return -1


print(Solution().snakesAndLadders([
    [-1, -1, 19, 10, -1],
    [2, -1, -1, 6, -1],
    [-1, 17, -1, 19, -1],
    [25, -1, 20, -1, -1],
    [-1, -1, -1, -1, 15]
]))
# @lc code=end
