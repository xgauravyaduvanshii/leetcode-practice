// LeetCode 3878. Count Good Subarrays — Hard
// https://leetcode.com/problems/count-good-subarrays/
// Submission 2203338389 — Accepted, Java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long countGoodSubarrays(int[] nums) {
        // My thinking: a subarray is good exactly when its
        // bitwise OR equals one of its elements. The OR is
        // numerically at least as large as every element in
        // the subarray, so it can only equal an element that
        // carries all of the OR's bits — that is, an element
        // equal to the OR itself. Fix the right end r: the
        // distinct ORs of subarrays ending at r are at most
        // 30, each covering a contiguous range of left ends.
        // For a group with OR v, the subarrays in it are
        // good exactly for the left ends at or before the
        // latest occurrence of v, which a hash map tracks as
        // r moves. The answer can reach about n^2 / 2, so it
        // is long.
        long ans = 0;
        List<int[]> ors = new ArrayList<>();
        Map<Integer, Integer> last = new HashMap<>();
        for (int r = 0; r < nums.length; r++) {
            int x = nums[r];
            last.put(x, r);
            List<int[]> next = new ArrayList<>();
            next.add(new int[]{x, 1});
            for (int[] p : ors) {
                int nv = p[0] | x;
                if (nv == next.get(next.size() - 1)[0]) {
                    next.get(next.size() - 1)[1] += p[1];
                } else {
                    next.add(new int[]{nv, p[1]});
                }
            }
            ors = next;
            int end = r;
            for (int[] p : ors) {
                int start = end - p[1] + 1;
                int pos = last.getOrDefault(p[0], -1);
                if (pos >= start) {
                    ans += Math.min(end, pos) - start + 1;
                }
                end = start - 1;
            }
        }
        return ans;
    }
}
