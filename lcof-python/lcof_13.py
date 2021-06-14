"""
剑指 Offer 13. 机器人的运动范围
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def digitsum(num):
            ans = 0
            while num:
                ans += num % 10
                num //= 10
            return ans

        cache = [(0, 0)]
        s = []

        while cache:
            x, y = cache.pop(0)
            if (x, y) not in s and x < m and y < n and digitsum(x) + digitsum(y) <= k:
                s.append((x, y))
                cache.extend([(x + 1, y), (x, y + 1)])

        return len(s)
