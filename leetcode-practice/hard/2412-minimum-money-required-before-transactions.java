// LeetCode 2412. Minimum Money Required Before Transactions — Hard
// https://leetcode.com/problems/minimum-money-required-before-transactions/
// Submission 2201726458 — Accepted, Java
//
// My thinking: the worst order runs every
// losing deal first — a deal done after
// them all must be paid for out of what is
// left, so I add every loss to the dearest
// gaining deal's cost and to the biggest
// cashback a losing deal ever returns, and
// take the larger of the two.

class Solution {
    public long minimumMoney(int[][] transactions) {
        long totalLoss = 0;
        long maxCostGain = 0;
        long maxCashbackLoss = 0;
        for (int[] t : transactions) {
            long cost = t[0], cashback = t[1];
            if (cost > cashback) {
                totalLoss += cost - cashback;
                maxCashbackLoss = Math.max(maxCashbackLoss, cashback);
            } else {
                maxCostGain = Math.max(maxCostGain, cost);
            }
        }
        return Math.max(totalLoss + maxCostGain, totalLoss + maxCashbackLoss);
    }
}
