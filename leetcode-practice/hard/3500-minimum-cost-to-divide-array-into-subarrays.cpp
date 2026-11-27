// LeetCode 3500. Minimum Cost to Divide Array Into Subarrays — Hard
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/
// Submission 2202719533 — Accepted, C++
#include <algorithm>
#include <deque>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int k) {
        // My thinking: let P and C be the prefix sums of nums and
        // cost. Splitting the first j elements into i subarrays
        // costs dp[i-1][m] + (P[j] + k*i) * (C[j] - C[m]) for the
        // last cut after m. Expanding, the m-part is a line in P[j]
        // with slope -C[m] and intercept dp[i-1][m] - k*i*C[m].
        // Costs are positive, so C[m] grows and the slopes arrive
        // in decreasing order while the queries P[j] grow, which
        // is exactly the monotone convex hull trick with a deque:
        // lines are added at the back and the best line is popped
        // from the front. All comparisons use integers (__int128
        // for the cross products), no floats.
        int n = (int)nums.size();
        vector<long long> P(n + 1, 0), C(n + 1, 0);
        for (int i = 0; i < n; i++) {
            P[i + 1] = P[i] + nums[i];
            C[i + 1] = C[i] + cost[i];
        }
        const long long INF = (long long)4e18;
        vector<long long> dpPrev(n + 1, INF), dpCur(n + 1, INF);
        dpPrev[0] = 0;
        long long ans = INF;
        auto bad = [](pair<long long, long long> l1, pair<long long, long long> l2,
                      pair<long long, long long> l3) {
            __int128 left = (__int128)(l2.second - l1.second) * (l2.first - l3.first);
            __int128 right = (__int128)(l3.second - l2.second) * (l1.first - l2.first);
            return left >= right;
        };
        auto ev = [](pair<long long, long long> ln, long long x) {
            return ln.first * x + ln.second;
        };
        for (int i = 1; i <= n; i++) {
            deque<pair<long long, long long>> dq;
            fill(dpCur.begin(), dpCur.end(), INF);
            for (int j = 1; j <= n; j++) {
                int m = j - 1;
                if (m >= i - 1 && dpPrev[m] < INF) {
                    pair<long long, long long> nl = {-C[m], dpPrev[m] - (long long)k * i * C[m]};
                    while (dq.size() >= 2 && bad(dq[dq.size() - 2], dq[dq.size() - 1], nl)) dq.pop_back();
                    dq.push_back(nl);
                }
                if (!dq.empty()) {
                    long long x = P[j];
                    while (dq.size() >= 2 && ev(dq[0], x) >= ev(dq[1], x)) dq.pop_front();
                    dpCur[j] = (P[j] + (long long)k * i) * C[j] + ev(dq[0], x);
                }
            }
            dpPrev = dpCur;
            ans = min(ans, dpPrev[n]);
        }
        return ans;
    }
};
