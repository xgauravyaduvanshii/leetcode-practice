#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int createSortedArray(vector<int>& instructions) {
        // My thinking: each new number costs the smaller of
        // how many are already below it and how many are
        // above it — a Fenwick tree keeps both counts cheap.
        const int MOD = 1000000007;
        vector<int> vals = instructions;
        sort(vals.begin(), vals.end());
        vals.erase(unique(vals.begin(), vals.end()), vals.end());
        int n = vals.size();
        vector<int> bit(n + 2, 0);
        auto add = [&](int i, int delta) {
            while (i <= n) { bit[i] += delta; i += i & -i; }
        };
        auto prefix = [&](int i) {
            int s = 0;
            while (i > 0) { s += bit[i]; i -= i & -i; }
            return s;
        };
        long long cost = 0;
        int total = 0;
        for (int x : instructions) {
            int i = lower_bound(vals.begin(), vals.end(), x) - vals.begin() + 1;
            int smaller = prefix(i - 1);
            int greater = total - prefix(i);
            cost = (cost + min(smaller, greater)) % MOD;
            add(i, 1);
            total++;
        }
        return (int)cost;
    }
};
