// LeetCode 2111. Minimum Operations to Make the Array K-Increasing — Hard
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/
// Submission 2201577245 — Accepted, Java
//
// My thinking: one operation rewrites a single
// element to anything, so the elements I leave
// alone have to already rise along their chain
// — each of the k chains keeps its longest
// non-decreasing run, and everything else is
// one operation each.

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int kIncreasing(int[] arr, int k) {
        int ops = 0;
        for (int start = 0; start < k; start++) {
            List<Integer> tails = new ArrayList<>();
            for (int i = start; i < arr.length; i += k) {
                int x = arr[i];
                int pos = upperBound(tails, x);
                if (pos == tails.size()) {
                    tails.add(x);
                } else {
                    tails.set(pos, x);
                }
            }
            int chainLen = (arr.length - 1 - start) / k + 1;
            ops += chainLen - tails.size();
        }
        return ops;
    }

    // First index whose value is greater than x.
    private int upperBound(List<Integer> tails, int x) {
        int lo = 0, hi = tails.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (tails.get(mid) <= x) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
