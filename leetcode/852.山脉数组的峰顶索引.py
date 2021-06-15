#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 1
        end = n - 2
        while start <= end:
            mid = (start + end) // 2
            if arr[mid + 1] <= arr[mid] >= arr[mid - 1]:
                return mid
            if arr[mid + 1] > arr[mid]:
                start = mid + 1
            elif arr[mid] < arr[mid - 1]:
                end = mid - 1
        return -1

# @lc code=end
