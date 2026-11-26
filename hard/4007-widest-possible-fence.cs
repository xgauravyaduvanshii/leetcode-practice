// LeetCode 4007. Widest Possible Fence — Hard
// https://leetcode.com/problems/widest-possible-fence/
// Submission 2203506781 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumWidth(int[] planks) {
        // My thinking: for a target height h, the fence can
        // use every plank of height h as is, plus disjoint
        // pairs of planks that add up to h. A pair summing
        // to h uses two planks both shorter than h, so the
        // singles and the pairs never compete for planks,
        // and pairs of different value splits (v, h-v) never
        // share a plank either. So for each h the best count
        // is freq[h] plus, over every value split, the pairs
        // that split can supply: min(freq[v], freq[h-v]) for
        // v < h-v, and freq[v] // 2 for v == h-v. Instead of
        // scoring every h from scratch, group by pair sum:
        // each pair of distinct values (v, w) contributes
        // min(freq[v], freq[w]) pairs to the sum v + w, and
        // each value contributes freq[v] // 2 pairs to 2v.
        // Then the answer is the best freq[h] + pairs[h]
        // over all heights and pair sums. A single plank
        // alone always works, so the answer is at least 1.
        var freq = new Dictionary<long, int>();
        foreach (int p in planks) {
            freq[p] = freq.TryGetValue(p, out int c) ? c + 1 : 1;
        }
        var vals = new List<long>(freq.Keys);
        vals.Sort();
        var pairs = new Dictionary<long, int>();
        for (int i = 0; i < vals.Count; i++) {
            long v = vals[i];
            long s2 = 2 * v;
            pairs[s2] = (pairs.TryGetValue(s2, out int c0) ? c0 : 0) + freq[v] / 2;
            for (int j = i + 1; j < vals.Count; j++) {
                long w = vals[j];
                long s = v + w;
                int add = Math.Min(freq[v], freq[w]);
                pairs[s] = (pairs.TryGetValue(s, out int c1) ? c1 : 0) + add;
            }
        }
        int ans = 1;
        var heights = new HashSet<long>(freq.Keys);
        heights.UnionWith(pairs.Keys);
        foreach (long h in heights) {
            int f = freq.TryGetValue(h, out int cf) ? cf : 0;
            int pr = pairs.TryGetValue(h, out int cp) ? cp : 0;
            ans = Math.Max(ans, f + pr);
        }
        return ans;
    }
}
