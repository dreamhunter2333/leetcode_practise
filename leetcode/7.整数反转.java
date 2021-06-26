/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
    public int reverse(int x) {
        int res = 0;
        while (x != 0) {
            if (res < Integer.MIN_VALUE / 10 || res > Integer.MAX_VALUE / 10)
                return 0;
            int temp = x % 10;
            x = x / 10;
            res = 10 * res + temp;
        }
        return res;
    }

    // public static void main(String[] args) {
    //     Solution s = new Solution();
    //     System.out.println(s.reverse(1234));
    // }
}
// @lc code=end
