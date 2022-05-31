// https://leetcode.com/problems/gas-station/

// There are n gas stations along a circular route,
// where the amount of gas at the ith station is gas[i].

// You have a car with an unlimited gas tank
// and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
// You begin the journey with an empty tank at one of the gas stations.

// Given two integer arrays gas and cost, return the starting gas station's index
// if you can travel around the circuit once in the clockwise direction, otherwise return -1.
// If there exists a solution, it is guaranteed to be unique.



class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        for (int i = 0; i < n; i++) {
            int j = i;
            int remain = gas[i];
            while (remain - cost[j] >= 0) {
                //减去花费的加上新的点的补给
                remain = remain - cost[j] + gas[(j + 1) % n];
                j = (j + 1) % n;
                //j 回到了 i
                if (j == i) {
                    return i;
                }
            }
            //最远距离绕到了之前，所以 i 后边的都不可能绕一圈了
            if (j < i) {
                return -1;
            }
            //i 直接跳到 j，外层 for 循环执行 i++，相当于从 j + 1 开始考虑
            i = j;

        }
        return -1;
    }
}
