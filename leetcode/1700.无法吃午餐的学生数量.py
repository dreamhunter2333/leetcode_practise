#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

from typing import List

# @lc code=start


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unlike_count = 0
        remain_count = len(students)
        while sandwiches and unlike_count != remain_count:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                unlike_count = 0
                remain_count -= 1
                continue
            unlike_count += 1
            students.append(students.pop(0))
        return len(students)


# @lc code=end
print(Solution().countStudents(
    students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]
))
print(Solution().countStudents(
    students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]
))
