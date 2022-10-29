#
# @lc app=leetcode.cn id=1773 lang=python3
#
# [1773] 统计匹配检索规则的物品数量
#

from typing import List


# @lc code=start
class Solution:

    rule_map = {"type": 0, "color": 1, "name": 2}

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(
            1
            for item in items
            if item[self.rule_map[ruleKey]] == ruleValue
        )


# @lc code=end
print(Solution().countMatches(
    items=[
        ["phone", "blue", "pixel"],
        ["computer", "silver", "lenovo"],
        ["phone", "gold", "iphone"]],
    ruleKey="color", ruleValue="silver"
))
print(Solution().countMatches(
    items=[
        ["phone", "blue", "pixel"],
        ["computer", "silver", "phone"],
        ["phone", "gold", "iphone"]],
    ruleKey="type", ruleValue="phone"
))
