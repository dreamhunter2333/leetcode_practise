package com.dreamhunter;

public class LcOf04 {

    // 暴力遍历
    public static boolean findNumberIn2DArray1(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;

        for (int[] numbers : matrix) {
            for (int number : numbers) {
                if (number == target)
                    return true;
            }
        }

        return false;
    }

    // 根据递增线性查找
    public static boolean findNumberIn2DArray2(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;

        int n = matrix.length;
        int x = 0;
        int y = matrix[0].length - 1;

        // 从右上角开始查询，大于左移，小于下移，等于返回
        while (x < n && y >= 0) {
            int number = matrix[x][y];
            if (number == target)
                return true;
            if (number > target){
                y--;
                continue;
            }
            x++;
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(findNumberIn2DArray2(
                new int[][]{{2,5},{2,8},{7,9},{7,11},{9,11}},
                7
        ));
    }
}

