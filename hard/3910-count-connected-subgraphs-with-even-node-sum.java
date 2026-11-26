// LeetCode 3910. Count Connected Subgraphs with Even Node Sum — Hard
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/
// Submission 2203379475 — Accepted, Java
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int evenSumSubgraphs(int[] nums, int[][] edges) {
        // My thinking: n is at most 13, so there are only
        // 8191 non-empty subsets — enumerate them all. A
        // subset has an even sum exactly when it holds an
        // even number of 1-valued nodes, which is a single
        // parity check on the subset masked with the
        // 1-valued nodes. A subset is connected when a
        // flood fill from its lowest set bit, walking only
        // to neighbours inside the subset, reaches every
        // node of the subset. Count the subsets that pass
        // both tests.
        int n = nums.length;
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        int ones = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 1) {
                ones |= 1 << i;
            }
        }
        int ans = 0;
        for (int mask = 1; mask < (1 << n); mask++) {
            if (Integer.bitCount(mask & ones) % 2 == 1) {
                continue;
            }
            int start = Integer.numberOfTrailingZeros(mask);
            int seen = 1 << start;
            ArrayDeque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            while (!stack.isEmpty()) {
                int u = stack.pop();
                for (int w : adj.get(u)) {
                    if (((mask >> w) & 1) == 1 && ((seen >> w) & 1) == 0) {
                        seen |= 1 << w;
                        stack.push(w);
                    }
                }
            }
            if (seen == mask) {
                ans++;
            }
        }
        return ans;
    }
}
