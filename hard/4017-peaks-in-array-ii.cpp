// LeetCode 4017. Peaks in Array II — Hard
// https://leetcode.com/problems/peaks-in-array-ii/
// Submission 2203513289 — Accepted, C++
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    vector<long long> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        // My thinking: a subarray is a peak subarray when
        // it holds a peak strictly inside it. Split the
        // query range [l, r] at its peaks p1 < ... < pm
        // (with p0 = l and p(m+1) = r as boundaries): a
        // subarray of length at least 3 has no peak inside
        // exactly when both ends fall in one gap between
        // consecutive boundaries, and gap t of length g
        // holds C(g, 2) such subarrays. So the answer is
        // C(r-l+1, 2) - (r-l) - sum C(g, 2) over the gaps,
        // which simplifies to ((r-l)^2 - sum g^2) / 2.
        // Expanding sum g^2 over the gaps and telescoping
        // the peak products gives r*(b-l) - W + a*(l-q),
        // where a = p1 is the first peak in (l, r),
        // b = pm is the last peak, q is the peak just
        // before a (0 if there is none), and W is the sum
        // of p*(p - prev(p)) over the peaks in (l, r),
        // with prev(p) the previous peak in the whole
        // array (0 if there is none). A Fenwick tree holds
        // those p*(p - prev(p)) values, and an ordered set
        // holds the peaks, so a query reads a, b, q and W
        // in O(log n). An update only changes peak status
        // at i-1, i, i+1 and the value of the next peak
        // after each of those, so refresh exactly those.
        int n = (int)nums.size();
        auto isPeak = [&](int k) {
            return k > 0 && k < n - 1 && nums[k] > nums[k - 1] && nums[k] > nums[k + 1];
        };
        set<int> peaks;
        for (int k = 1; k < n - 1; k++) {
            if (isPeak(k)) peaks.insert(k);
        }
        vector<long long> bit(n + 2, 0);
        auto bitAdd = [&](int i, long long d) {
            for (i += 1; i <= n + 1; i += i & -i) bit[i] += d;
        };
        auto bitSum = [&](int i) {
            long long s = 0;
            for (; i > 0; i -= i & -i) s += bit[i];
            return s;
        };
        auto peakValue = [&](int p) {
            auto it = peaks.lower_bound(p);
            long long prv = (it == peaks.begin()) ? 0 : (long long)*prev(it);
            return (long long)p * (p - prv);
        };
        for (int p : peaks) bitAdd(p, peakValue(p));

        vector<long long> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int l = q[1], r = q[2];
                auto itlo = peaks.upper_bound(l);
                auto ithi = peaks.lower_bound(r);
                if (itlo == ithi) {
                    ans.push_back(0);
                    continue;
                }
                long long a = *itlo;
                long long b = *prev(ithi);
                long long prevA = (itlo == peaks.begin()) ? 0 : (long long)*prev(itlo);
                long long w = bitSum((int)b + 1) - bitSum((int)a);
                ans.push_back((long long)r * (b - l) - w + a * (l - prevA));
            } else {
                int i = q[1], val = q[2];
                set<int> refresh;
                for (int k : {i - 1, i, i + 1}) {
                    if (k >= 1 && k <= n - 2) {
                        refresh.insert(k);
                        auto it = peaks.upper_bound(k);
                        if (it != peaks.end()) refresh.insert(*it);
                    }
                }
                for (int p : refresh) {
                    if (peaks.count(p)) bitAdd(p, -peakValue(p));
                }
                for (int k : {i - 1, i, i + 1}) {
                    if (k >= 1 && k <= n - 2) peaks.erase(k);
                }
                nums[i] = val;
                for (int k : {i - 1, i, i + 1}) {
                    if (k >= 1 && k <= n - 2 && isPeak(k)) peaks.insert(k);
                }
                for (int p : refresh) {
                    if (peaks.count(p)) bitAdd(p, peakValue(p));
                }
            }
        }
        return ans;
    }
};
