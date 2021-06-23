import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为K的子数组
 */

// @lc code=start
class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int numSum = 0;
        Map<Integer, Integer> sumMap = new HashMap<>();
        sumMap.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            numSum += nums[i];
            if (sumMap.containsKey(numSum - k)) {
                res += sumMap.get(numSum - k);
            }
            sumMap.put(numSum, sumMap.getOrDefault(numSum, 0) + 1);
        }
        return res;
    }

    // public static void main(String[] args) {
    // int[] nums = new int[] {1, 1, 1};
    // Solution solution = new Solution();
    // System.out.println(solution.subarraySum(nums, 2));
    // }
}
// @lc code=end
