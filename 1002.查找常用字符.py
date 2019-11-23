#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (65.09%)
# Likes:    42
# Dislikes: 0
# Total Accepted:    7.2K
# Total Submissions: 11.1K
# Testcase Example:  '["bella","label","roller"]'
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
# 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 
# 你可以按任意顺序返回答案。
# 
# 
# 
# 示例 1：
# 
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
# 
# 
# 示例 2：
# 
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母
# 
# 
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = {}
        return_list = []
        for index in range(len(A)):
            a_list = list(A[index])
            if index == 0:
                for key in a_list:
                    if result.get(key):
                        result[key] += 1
                    else:
                        result[key] = 1
            else:
                new_result = {}
                for key in a_list:
                    if result.get(key):
                        if new_result.get(key):
                            new_result[key] += 1
                        else:
                            new_result[key] = 1
                for key in new_result.keys():
                    new_result[key] = min(result[key], new_result[key])
                result = new_result
        for key in result.keys():
            for _ in range(result[key]):
                return_list.append(key)
        return return_list

# @lc code=end

