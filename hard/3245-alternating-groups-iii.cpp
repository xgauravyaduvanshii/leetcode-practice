// LeetCode 3245. Alternating Groups III — Hard
// https://leetcode.com/problems/alternating-groups-iii/
// Submission 2202135694 — Accepted, C++
//
// My thinking: positions where neighbours are
// equal ("bad" edges) split the circle into
// alternating blocks. A block of length L holds
// max(0, L - k + 1) alternating groups of size
// k. I keep the bad edges in a set and two
// Fenwick trees over block lengths (count and
// sum), so a colour flip only touches the two
// blocks next to it and every query is O(log n).

#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n = 0;
    vector<long long> bit;
    Fenwick() {}
    Fenwick(int n_) : n(n_), bit(n_ + 1, 0) {}
    void add(int idx, long long delta) {
        for (; idx <= n; idx += idx & -idx) bit[idx] += delta;
    }
    long long sumPrefix(int idx) const {
        long long s = 0;
        for (; idx > 0; idx -= idx & -idx) s += bit[idx];
        return s;
    }
};

class Solution {
public:
    vector<int> numberOfAlternatingGroups(vector<int>& colors, vector<vector<int>>& queries) {
        int n = (int)colors.size();
        Fenwick bitC(n), bitS(n);
        auto blockAdd = [&](int len, int delta) {
            bitC.add(len, delta);
            bitS.add(len, (long long)delta * len);
        };
        auto dist = [&](int a, int b) {
            int d = b - a;
            if (d <= 0) d += n;
            return d;
        };
        set<int> bad;
        for (int i = 0; i < n; i++) {
            if (colors[i] == colors[(i + 1) % n]) bad.insert(i);
        }
        for (auto it = bad.begin(); it != bad.end(); ++it) {
            auto nxt = next(it);
            if (nxt == bad.end()) nxt = bad.begin();
            blockAdd(dist(*it, *nxt), 1);
        }
        function<void(int)> addBad = [&](int e) {
            if (bad.empty()) {
                blockAdd(n, 1);
                bad.insert(e);
                return;
            }
            auto it = bad.lower_bound(e);
            int succ = (it == bad.end() ? *bad.begin() : *it);
            int pred;
            if (it == bad.begin()) pred = *bad.rbegin();
            else { auto it2 = it; --it2; pred = *it2; }
            blockAdd(dist(pred, succ), -1);
            blockAdd(dist(pred, e), 1);
            blockAdd(dist(e, succ), 1);
            bad.insert(e);
        };
        function<void(int)> removeBad = [&](int e) {
            if (bad.size() == 1) {
                blockAdd(n, -1);
                bad.erase(e);
                return;
            }
            auto it = bad.find(e);
            auto itSucc = next(it);
            if (itSucc == bad.end()) itSucc = bad.begin();
            int succ = *itSucc;
            int pred;
            if (it == bad.begin()) pred = *bad.rbegin();
            else { auto it2 = it; --it2; pred = *it2; }
            blockAdd(dist(pred, e), -1);
            blockAdd(dist(e, succ), -1);
            blockAdd(dist(pred, succ), 1);
            bad.erase(it);
        };
        vector<int> ans;
        for (auto &q : queries) {
            if (q[0] == 1) {
                int k = q[1];
                if (bad.empty()) {
                    ans.push_back(n);
                } else {
                    long long cntGe = (long long)bad.size() - bitC.sumPrefix(k - 1);
                    long long sumGe = (long long)n - bitS.sumPrefix(k - 1);
                    ans.push_back((int)(sumGe - (long long)(k - 1) * cntGe));
                }
            } else {
                int idx = q[1];
                int col = q[2];
                if (colors[idx] == col) continue;
                int prev = colors[(idx - 1 + n) % n];
                int nxt = colors[(idx + 1) % n];
                int old = colors[idx];
                int e1 = (idx - 1 + n) % n;
                int e2 = idx;
                bool was1 = prev == old, now1 = prev == col;
                bool was2 = old == nxt, now2 = col == nxt;
                colors[idx] = col;
                if (was1 != now1) {
                    if (now1) addBad(e1); else removeBad(e1);
                }
                if (was2 != now2) {
                    if (now2) addBad(e2); else removeBad(e2);
                }
            }
        }
        return ans;
    }
};
