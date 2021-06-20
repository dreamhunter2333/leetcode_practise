#
# @lc app=leetcode.cn id=1600 lang=python3
#
# [1600] 皇位继承顺序
#

# @lc code=start
from typing import List


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.name_map = {
            kingName: {
                'child': [],
                'alive': True
            }
        }
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.name_map[parentName]['child'].append(childName)
        self.name_map[childName] = {
            'child': [],
            'alive': True
        }

    def death(self, name: str) -> None:
        self.name_map[name]['alive'] = False

    def getInheritanceOrder(self) -> List[str]:

        res = []

        def dfs(name: str):
            if self.name_map[name]['alive']:
                res.append(name)
            for child in self.name_map[name]['child']:
                dfs(child)

        dfs(self.king)

        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance('king')
# obj.birth("king", "andy")
# obj.birth("king", "bob")
# obj.birth("king", "catherine")
# obj.birth("andy", "matthew")
# obj.birth("bob", "alex")
# obj.birth("bob", "asha")
# obj.birth("bob", "alex")
# print(obj.getInheritanceOrder())
# obj.death("bob")
# print(obj.getInheritanceOrder())

# @lc code=end
