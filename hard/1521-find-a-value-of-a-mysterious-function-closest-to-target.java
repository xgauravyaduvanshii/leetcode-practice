class Solution {
    public int closestToTarget(int[] arr, int target) {
        // My thinking: the AND of a subarray can only lose
        // bits as it grows — so keep the handful of distinct
        // values ending here and check each against the target.
        int best = Integer.MAX_VALUE;
        java.util.Set<Integer> cur = new java.util.HashSet<>();
        for (int x : arr) {
            java.util.Set<Integer> next = new java.util.HashSet<>();
            next.add(x);
            for (int v : cur) next.add(x & v);
            cur = next;
            for (int v : cur) best = Math.min(best, Math.abs(v - target));
        }
        return best;
    }
}
