// LeetCode 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K — Hard
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/
// Submission 2202766029 — Accepted, C#
public class Solution {
    public int MaxProduct(int[] nums, int k, int limit) {
        // My thinking: I walk the array once, keeping for every
        // reachable (alternating sum, parity of length) the set of
        // products that stay within the limit. Reachability is tracked
        // on its own, apart from the products: a partial product that
        // already exceeds the limit is still a live subsequence, because
        // a later 0 multiplies it back to 0, which is within the limit.
        // Dropping over-limit states loses exactly those rescues, so I
        // keep the state reachable and only add a 0 product when a 0
        // arrives. Keeping the whole set of products (not just the max)
        // matters too, because a smaller product can survive a later
        // multiplication that pushes the largest one over the limit.
        var reach = new HashSet<(int, int)> { (0, 0) };
        var prod = new Dictionary<(int, int), HashSet<int>> {
            [(0, 0)] = new HashSet<int>()
        };
        foreach (int v in nums) {
            var items = new List<(int, int)>(reach);
            var snapshot = new Dictionary<(int, int), HashSet<int>>();
            foreach (var kv in prod) snapshot[kv.Key] = new HashSet<int>(kv.Value);
            foreach (var (s, p) in items) {
                int ns = p == 0 ? s + v : s - v;
                int np = 1 - p;
                reach.Add((ns, np));
                if (!prod.TryGetValue((ns, np), out var cur)) {
                    cur = new HashSet<int>();
                    prod[(ns, np)] = cur;
                }
                if (snapshot.TryGetValue((s, p), out var oldSet)) {
                    foreach (int p2 in oldSet) {
                        int nv = p2 * v;
                        if (nv <= limit) cur.Add(nv);
                    }
                }
                if (v == 0) cur.Add(0);
            }
            reach.Add((v, 1));
            if (v <= limit) {
                if (!prod.TryGetValue((v, 1), out var cur)) {
                    cur = new HashSet<int>();
                    prod[(v, 1)] = cur;
                }
                cur.Add(v);
            }
        }
        int best = -1;
        foreach (int p in new[] { 0, 1 }) {
            if (prod.TryGetValue((k, p), out var set)) {
                foreach (int val in set) best = Math.Max(best, val);
            }
        }
        return best;
    }
}
