// LeetCode 3086. Minimum Moves to Pick K Ones — Hard
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/
// Submission 2201983118 — Accepted, C++
//
// My thinking: I collect the positions of
// the ones. Gathering a run of consecutive
// ones is cheapest around their median,
// and prefix sums give that cost in
// constant time. Either I gather
// k - maxChanges existing ones and change
// the rest (two moves per change), or I
// gather just one, two or three ones and
// change the rest — a small gathered run
// can sit next to the changed ones. I try
// every window and keep the cheapest total.

class Solution {
public:
    long long minimumMoves(vector<int>& nums, int k, int maxChanges) {
        vector<long long> pos;
        for (int i = 0; i < (int)nums.size(); ++i)
            if (nums[i] == 1) pos.push_back(i);
        int m = (int)pos.size();
        vector<long long> pref(m + 1, 0);
        for (int i = 0; i < m; ++i) pref[i + 1] = pref[i] + pos[i];
        auto gather = [&](int l, int r) -> long long {
            if (r - l <= 1) return 0;
            int mid = (l + r) / 2;
            long long median = pos[mid];
            long long left = median * (mid - l) - (pref[mid] - pref[l]);
            long long right = (pref[r] - pref[mid + 1]) - median * (r - mid - 1);
            return left + right;
        };
        const long long INF = (long long)4e18;
        long long ans = INF;
        int L = k - maxChanges;
        if (L <= 0) ans = min(ans, 2LL * k);
        if (L > 0 && L <= m) {
            long long best = INF;
            for (int i = 0; i + L <= m; ++i) best = min(best, gather(i, i + L));
            ans = min(ans, best + 2LL * maxChanges);
        }
        for (int s = 1; s <= 3; ++s) {
            if (s < L || s > k || s > m) continue;
            for (int i = 0; i + s <= m; ++i)
                ans = min(ans, gather(i, i + s) + 2LL * (k - s));
        }
        return ans;
    }
};
