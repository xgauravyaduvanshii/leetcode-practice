// LeetCode 3117. Minimum Sum of Values by Dividing Array — Hard
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/
// Submission 2202010290 — Accepted, Java
//
// My thinking: I scan the array keeping
// a small map from (segments finished,
// running AND of the current segment) to
// the cheapest cost so far. The AND only
// ever loses bits, so few states survive.
// When a segment's AND reaches its
// target I may close it, adding the
// segment's last element to the cost;
// the answer is the cheapest cost with
// all segments closed.

import java.util.*;

class Solution {
    public int minimumValueSum(int[] nums, int[] andValues) {
        int m = andValues.length;
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);
        for (int x : nums) {
            Map<Integer, Integer> ndp = new HashMap<>();
            for (Map.Entry<Integer, Integer> e : dp.entrySet()) {
                int key = e.getKey();
                int cost = e.getValue();
                int j = key >> 18;
                int cur = (key & 262143) - 1;
                if (cur == -1) {
                    if (j >= m) continue;
                    int target = andValues[j];
                    if ((x & target) != target) continue;
                    int k2 = (j << 18) | (x + 1);
                    ndp.merge(k2, cost, Integer::min);
                    if (x == target) {
                        int k3 = (j + 1) << 18;
                        ndp.merge(k3, cost + x, Integer::min);
                    }
                } else {
                    int target = andValues[j];
                    int nc = cur & x;
                    if ((nc & target) != target) continue;
                    int k2 = (j << 18) | (nc + 1);
                    ndp.merge(k2, cost, Integer::min);
                    if (nc == target) {
                        int k3 = (j + 1) << 18;
                        ndp.merge(k3, cost + x, Integer::min);
                    }
                }
            }
            dp = ndp;
            if (dp.isEmpty()) break;
        }
        return dp.getOrDefault(m << 18, -1);
    }
}
