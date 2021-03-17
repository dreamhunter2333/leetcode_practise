package com.dreamhunter;

import java.util.Arrays;
import java.util.HashSet;

/**
 * 找出数组中重复的数字
 *
 * 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
 * 数组中某些数字是重复的，但不知道有几个数字重复了，
 * 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
 *
 * 示例 1：
 *
 * 输入：
 * [2, 3, 1, 0, 2, 5, 3]
 * 输出：2 或 3
 *
 * 限制：2 <= n <= 100000
*/
public class LcOf03 {

    // 哈希表 5 ms
    public static int findRepeatNumber1(int[] nums) {
        HashSet<Integer> oldNum = new HashSet<>();
        for (int i : nums) {
            if (!oldNum.add(i)) return i;
        }
        return -1;
    }

    // 排序 3 ms
    public static int findRepeatNumber2(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) return nums[i];
        }
        return -1;
    }

    // 原地交换 0 ms
    public static int findRepeatNumber3(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            // 位置错误时进行交换
            while (nums[i] != i) {
                // 如果交换的目标位置和当前位置的值相等，即重复
                if (nums[nums[i]] == nums[i]) return nums[i];
                // 交换位置，使 i 位置的元素正确
                int temp = nums[i];
                nums[i] = nums[temp];
                nums[temp] = temp;
            }
        }
        return -1;
    }

    // 数组标记 2 ms
    public static int findRepeatNumber4(int[] nums) {
        boolean[] flags = new boolean[100000];
        for (int i : nums) {
            if (flags[i]) return i;
            flags[i] = true;
        }
        return -1;
    }

    public static void main(String[] args) {
        System.out.println(findRepeatNumber1(new int[]{2, 3, 1, 0, 2, 5, 3}));
        System.out.println(findRepeatNumber2(new int[]{2, 3, 1, 0, 2, 5, 3}));
        System.out.println(findRepeatNumber3(new int[]{2, 3, 1, 0, 2, 5, 3}));
        System.out.println(findRepeatNumber4(new int[]{2, 3, 1, 0, 2, 5, 3}));
    }
}
