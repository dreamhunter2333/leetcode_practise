#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

from typing import List


# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        i = 0
        n = len(asteroids)
        while i < n:
            asteroid = asteroids[i]
            if not res or not (
                res[-1] > 0 and asteroid < 0
            ):
                res.append(asteroid)
                i += 1
                continue
            if abs(asteroid) > res[-1] > 0:
                res.pop()
                continue
            if abs(asteroid) == abs(res[-1]):
                res.pop()
            i += 1

        return res


# @lc code=end
print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
print(Solution().asteroidCollision([-2, -2, 1, -2]))
