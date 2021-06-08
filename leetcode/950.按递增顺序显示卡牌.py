#
# @lc app=leetcode.cn id=950 lang=python3
#
# [950] 按递增顺序显示卡牌
#

# @lc code=start
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # 逆操作
        res = []
        deck.sort()
        while deck:
            res.append(deck.pop())
            if len(res) > 1 and deck:
                res.append(res.pop(0))
        return list(reversed(res))


print(Solution().deckRevealedIncreasing(list(range(1, 5))))
# @lc code=end
