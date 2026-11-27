// LeetCode 4055. Count Shadow Pairs II — Hard
// https://leetcode.com/problems/count-shadow-pairs-ii/
// Submission 2203580931 — Accepted, C++
//
// My thinking: split the array in half and count
// cross pairs, then recurse. For i on the left let
// b[i] be the smallest value after i in the left
// half that is bigger than nums[i] (or infinity);
// for j on the right let c[j] be the largest value
// before j in the right half that is smaller than
// nums[j] (or zero). A cross pair is a shadow pair
// exactly when nums[i] < nums[j], b[i] >= nums[j]
// and c[j] <= nums[i]. Sweeping j by rising value
// with a Fenwick tree over the left values counts
// those i's, adding each i when it becomes eligible
// and dropping it once its b[i] bound is passed.

#include <vector>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int shadowPairs(vector<int>& nums) {
        return solve(nums, 0, (int)nums.size());
    }

private:
    static const int INF = 2000000000;

    // Fenwick tree for prefix sums over compressed values.
    struct Fenwick {
        int n;
        vector<int> bit;
        Fenwick(int n = 0) : n(n), bit(n + 1, 0) {}
        void add(int idx, int delta) {  // 0-based idx
            for (++idx; idx <= n; idx += idx & -idx) bit[idx] += delta;
        }
        int sumPrefix(int idx) const {  // sum of [0, idx)
            int s = 0;
            for (; idx > 0; idx -= idx & -idx) s += bit[idx];
            return s;
        }
        int rangeSum(int l, int r) const { return sumPrefix(r) - sumPrefix(l); }
    };

    int solve(vector<int>& a, int l, int r) {
        if (r - l <= 1) return 0;
        int m = (l + r) / 2;
        int ans = solve(a, l, m) + solve(a, m, r);

        // b[i] for i in [l, m): successor of a[i] among values to its right in the half.
        vector<int> b(m - l, INF);
        set<int> seen;
        for (int i = m - 1; i >= l; --i) {
            auto it = seen.upper_bound(a[i]);
            if (it != seen.end()) b[i - l] = *it;
            seen.insert(a[i]);
        }
        // c[j] for j in [m, r): predecessor of a[j] among values to its left in the half.
        vector<int> c(r - m, 0);
        seen.clear();
        for (int j = m; j < r; ++j) {
            auto it = seen.lower_bound(a[j]);
            if (it != seen.begin()) c[j - m] = *prev(it);
            seen.insert(a[j]);
        }

        // Left indices sorted by value, and by b bound.
        vector<int> L(m - l), Lb(m - l), R(r - m);
        for (int i = 0; i < m - l; ++i) L[i] = Lb[i] = i;
        for (int j = 0; j < r - m; ++j) R[j] = j;
        sort(L.begin(), L.end(), [&](int x, int y) { return a[l + x] < a[l + y]; });
        sort(Lb.begin(), Lb.end(), [&](int x, int y) { return b[x] < b[y]; });
        sort(R.begin(), R.end(), [&](int x, int y) { return a[m + x] < a[m + y]; });

        // Coordinate-compress the left values for the Fenwick tree.
        vector<int> comp(a.begin() + l, a.begin() + m);
        sort(comp.begin(), comp.end());
        comp.erase(unique(comp.begin(), comp.end()), comp.end());
        Fenwick ft((int)comp.size());
        auto idxOf = [&](int v) {
            return (int)(lower_bound(comp.begin(), comp.end(), v) - comp.begin());
        };

        vector<char> added(m - l, 0);
        size_t p = 0, q = 0;
        for (int jj : R) {
            int vj = a[m + jj];
            while (p < L.size() && a[l + L[p]] < vj) {
                int i = L[p];
                if (b[i] >= vj) {
                    ft.add(idxOf(a[l + i]), 1);
                    added[i] = 1;
                }
                ++p;
            }
            while (q < Lb.size() && b[Lb[q]] < vj) {
                int i = Lb[q];
                if (added[i]) {
                    ft.add(idxOf(a[l + i]), -1);
                    added[i] = 0;
                }
                ++q;
            }
            int lo = idxOf(c[jj]);  // c[jj] <= a[i] needed; c is 0 when none
            ans += ft.rangeSum(lo, (int)comp.size());
        }
        return ans;
    }
};
