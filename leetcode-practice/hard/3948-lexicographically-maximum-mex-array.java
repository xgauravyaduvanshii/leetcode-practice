// LeetCode 3948. Lexicographically Maximum MEX Array — Hard
// https://leetcode.com/problems/lexicographically-maximum-mex-array/
// Submission 2203445977 — Accepted, Java
class Solution {
    public int[] maximumMEX(int[] nums) {
        // My thinking: the MEX of a growing prefix never drops,
        // so the biggest first element we can ever produce is
        // the MEX of the whole remaining suffix — and the
        // shortest cut achieving it ends just after the last
        // of 0..MEX-1 first shows up. Taking that shortest cut
        // is also best for the rest: any longer first cut leaves
        // a suffix of the same tail, and the extra elements it
        // swallows can only raise the next MEX, never lower it.
        // So repeat: append the suffix MEX, cut right after its
        // last missing value appears (or after one element when
        // the MEX is 0). A frequency table of the suffix keeps
        // the MEX current as the start moves forward — removing
        // elements can only lower it — and each scan for the cut
        // advances the start, so the whole run is linear.
        int n = nums.length;
        int[] freq = new int[n + 2];
        for (int v : nums) if (v <= n) freq[v]++;
        int mex = 0;
        while (mex <= n && freq[mex] > 0) mex++;
        int[] res = new int[n];
        int r = 0, s = 0;
        while (s < n) {
            int m = mex;
            if (m == 0) {
                res[r++] = 0;
                int v = nums[s];
                if (v <= n) {
                    freq[v]--;
                    if (freq[v] == 0 && v < mex) mex = v;
                }
                s++;
                continue;
            }
            boolean[] seen = new boolean[m];
            int got = 0, i = s;
            while (got < m) {
                int v = nums[i];
                if (v < m && !seen[v]) {
                    seen[v] = true;
                    got++;
                }
                i++;
            }
            int k = i;
            res[r++] = m;
            for (int j = s; j < k; j++) {
                int v = nums[j];
                if (v <= n) {
                    freq[v]--;
                    if (freq[v] == 0 && v < mex) mex = v;
                }
            }
            s = k;
        }
        return java.util.Arrays.copyOf(res, r);
    }
}
