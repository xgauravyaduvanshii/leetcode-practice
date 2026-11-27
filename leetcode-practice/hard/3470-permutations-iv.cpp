// LeetCode 3470. Permutations IV — Hard
// https://leetcode.com/problems/permutations-iv/
// Submission 2202657973 — Accepted 999/999, C++
//
// My thinking: an alternating permutation must alternate odd and even, so
// once I pick a number the parity of every later slot is forced. I build
// the answer left to right, trying candidates in increasing order; for a
// candidate I count how many completions it leaves, which is (remaining
// odds)! times (remaining evens)! when the remaining counts exactly fill
// the forced odd and even slots, and 0 otherwise. If k is larger than that
// count I skip the whole block, otherwise I take the candidate and move on.
// A candidate whose parity matches the previous pick is never tried. The
// factorials are capped above k so the counts never overflow.

#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> permute(int n, int k) {
        const long long INF = (long long)4e18;
        auto fact = [&](int m) {
            long long r = 1;
            for (int i = 2; i <= m; i++) {
                r *= i;
                if (r > INF) return INF;
            }
            return r;
        };
        vector<int> odds, evens;
        for (int x = 1; x <= n; x++) (x % 2 == 1 ? odds : evens).push_back(x);

        auto completions = [&](vector<int> rem_o, vector<int> rem_e, int nxt) {
            int need_o = 0, need_e = 0, p = nxt;
            int L = (int)rem_o.size() + (int)rem_e.size();
            for (int i = 0; i < L; i++) {
                if (p == 1) need_o++;
                else need_e++;
                p = 1 - p;
            }
            if ((int)rem_o.size() != need_o || (int)rem_e.size() != need_e) return 0LL;
            long long a = fact((int)rem_o.size()), b = fact((int)rem_e.size());
            if (a > INF / max(1LL, b)) return INF;
            return a * b;
        };

        vector<int> res, rem_o = odds, rem_e = evens;
        int prev = -1;
        for (int pos = 0; pos < n; pos++) {
            vector<int> cands = rem_o;
            cands.insert(cands.end(), rem_e.begin(), rem_e.end());
            sort(cands.begin(), cands.end());
            bool done = false;
            for (int c : cands) {
                if (prev != -1 && (c % 2) == prev) continue;
                vector<int> no = rem_o, ne = rem_e;
                if (c % 2 == 1) no.erase(remove(no.begin(), no.end(), c), no.end());
                else ne.erase(remove(ne.begin(), ne.end(), c), ne.end());
                long long cnt = completions(no, ne, 1 - (c % 2));
                if (k > cnt) {
                    k -= (int)min<long long>(cnt, k);
                } else {
                    res.push_back(c);
                    rem_o = no;
                    rem_e = ne;
                    prev = c % 2;
                    done = true;
                    break;
                }
            }
            if (!done) return {};
        }
        return res;
    }
};
