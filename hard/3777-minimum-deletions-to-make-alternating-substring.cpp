// LeetCode 3777. Minimum Deletions to Make Alternating Substring — Hard
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/
// Submission 2203174254 — Accepted, C++
#include <string>
#include <vector>
using namespace std;

class Fenwick {
public:
    int n;
    vector<int> bit;
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) bit[i] += delta;
    }
    int prefix(int i) const {
        // My thinking: sum of the stored values at positions
        // 1..i (1-based), used for range sums below.
        int s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    }
};

class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        // My thinking: to make a string alternating by deleting
        // characters, every maximal run of equal letters of
        // length L must lose L - 1 of them, and that is exactly
        // the number of adjacent equal pairs inside the run.
        // So the deletions a substring needs equal the count of
        // positions i in [l, r-1] with s[i] == s[i+1]. Keep
        // those pair indicators in a Fenwick tree: a type-2
        // query is one range sum, and flipping s[j] only
        // changes the pairs ending at j-1 and j, so a type-1
        // query is two point updates.
        int n = (int)s.size();
        vector<int> bad(max(n - 1, 0), 0);
        Fenwick bit(max(n - 1, 1));
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                bad[i] = 1;
                bit.add(i + 1, 1);
            }
        }
        vector<int> ans;
        for (auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                s[j] = (s[j] == 'A' ? 'B' : 'A');
                for (int i : {j - 1, j}) {
                    if (0 <= i && i < n - 1) {
                        int nw = (s[i] == s[i + 1]) ? 1 : 0;
                        if (nw != bad[i]) {
                            bit.add(i + 1, nw - bad[i]);
                            bad[i] = nw;
                        }
                    }
                }
            } else {
                int l = q[1], r = q[2];
                // Pairs bad[l..r-1] sit at Fenwick positions
                // l+1..r, so the range sum is prefix(r) -
                // prefix(l).
                ans.push_back(bit.prefix(r) - bit.prefix(l));
            }
        }
        return ans;
    }
};
