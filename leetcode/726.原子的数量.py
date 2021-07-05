#
# @lc app=leetcode.cn id=726 lang=python3
#
# [726] 原子的数量
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def dfs(f):
            cache_map = defaultdict(int)
            i = 0
            n = len(f)
            while i < n:
                if ord('A') <= ord(f[i]) <= ord('Z'):
                    atom = f[i]
                    count = ""
                    i += 1
                    while i < n and ord('a') <= ord(f[i]) <= ord('z'):
                        atom += f[i]
                        i += 1
                    while i < n and f[i].isdigit():
                        count += f[i]
                        i += 1
                    cache_map[atom] += int(count) if count else 1
                elif f[i] == "(":
                    stack = ""
                    count = ""
                    flag = 1
                    i += 1
                    while i < n:
                        if f[i] == "(":
                            flag += 1
                        elif f[i] == ")":
                            flag -= 1
                        if flag == 0:
                            i += 1
                            break
                        stack += f[i]
                        i += 1
                    while i < n and f[i].isdigit():
                        count += f[i]
                        i += 1
                    count = int(count) if count else 1
                    for k, v in dfs(stack).items():
                        cache_map[k] += v * count

            return cache_map

        res = dfs(formula)

        return "".join(
            k if res[k] == 1 else k + str(res[k])
            for k in sorted(res, key=lambda a: a)
        )


print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
# @lc code=end
