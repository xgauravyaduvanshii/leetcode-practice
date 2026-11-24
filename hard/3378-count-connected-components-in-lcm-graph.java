// LeetCode 3378. Count Connected Components in LCM Graph — Hard
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/
// Submission 2202492100 — Accepted 697/697, Java
//
// My thinking: two numbers are joined exactly when they share a common
// multiple no bigger than threshold, because then their lcm divides that
// multiple and is at most threshold, and conversely their lcm itself is
// such a multiple. So for every multiple m up to threshold I union each
// number with the first divisor of m I have seen. Numbers above threshold
// have no multiple in range and stay alone.
class Solution {
    public int countComponents(int[] nums, int threshold) {
        int n = nums.length;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int[] pos = new int[threshold + 1];
        java.util.Arrays.fill(pos, -1);
        for (int i = 0; i < n; i++) {
            if (nums[i] <= threshold) pos[nums[i]] = i;
        }
        int[] first = new int[threshold + 1];
        java.util.Arrays.fill(first, -1);
        for (int x = 1; x <= threshold; x++) {
            int i = pos[x];
            if (i == -1) continue;
            for (int m = x; m <= threshold; m += x) {
                int j = first[m];
                if (j == -1) first[m] = i;
                else union(parent, i, j);
            }
        }
        int ans = 0;
        for (int x : nums) if (x > threshold) ans++;
        java.util.Set<Integer> roots = new java.util.HashSet<>();
        for (int i = 0; i < n; i++) {
            if (nums[i] <= threshold) roots.add(find(parent, i));
        }
        return ans + roots.size();
    }

    private int find(int[] parent, int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }

    private void union(int[] parent, int a, int b) {
        int ra = find(parent, a), rb = find(parent, b);
        if (ra != rb) parent[ra] = rb;
    }
}
