"""
剑指 Offer 38. 字符串的排列
"""
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        # 回溯法

        res = []
        n = len(s)
        chars = list(s)

        def dfs(start):
            if start == n:
                res.append(''.join(chars))
                return
            dfs(start+1)
            x = {chars[start]}
            for i in range(start+1, n):
                # 剪枝，不然会直接超时，去除重复的统计
                if chars[i] in x:
                    continue
                x.add(chars[i])
                chars[start], chars[i] = chars[i], chars[start]
                dfs(start+1)
                chars[i], chars[start] = chars[start], chars[i]

        dfs(0)

        return res


print(Solution().permutation("abc"))
