// LeetCode 3953. Maximum Score with Co-Prime Element — Hard
// https://leetcode.com/problems/maximum-score-with-co-prime-element/
// Submission 2203451853 — Accepted, C++
#include <vector>
using namespace std;

class Solution {
public:
    int maxScore(vector<int>& nums, int maxVal) {
        // My thinking: pick the selected value v and one index
        // to hold it. Every other element sharing a factor with
        // v must be changed, and changing it to 1 always works,
        // so the cost is fixed by v: if v already sits in the
        // array we keep that copy (cost = bad(v) - 1, the copy
        // itself being counted as bad when v > 1); if v is absent
        // we change some bad element into v instead (cost =
        // bad(v)), or pay 1 with no bad element at all. The
        // selected value may also be an untouched element larger
        // than maxVal — only changed values must fit under
        // maxVal. bad(v) is n minus the count of elements
        // co-prime to v, and that count comes from Mobius
        // inversion over v's divisors: sum mu(d) * (multiples
        // of d in nums), computed for all v at once with a
        // sieve over multiples.
        int n = (int)nums.size();
        int maxN = 0;
        for (int v : nums) maxN = max(maxN, v);
        int lim = max(maxVal, maxN);
        vector<int> freq(lim + 1, 0);
        for (int v : nums) freq[v]++;
        vector<int> cntMult(lim + 1, 0);
        for (int d = 1; d <= lim; d++)
            for (int m = d; m <= lim; m += d) cntMult[d] += freq[m];
        vector<int> mu(lim + 1, 0), primes;
        vector<int> isComp(lim + 1, 0);
        mu[1] = 1;
        for (int i = 2; i <= lim; i++) {
            if (!isComp[i]) {
                primes.push_back(i);
                mu[i] = -1;
            }
            for (int p : primes) {
                if (i * p > lim) break;
                isComp[i * p] = 1;
                if (i % p == 0) {
                    mu[i * p] = 0;
                    break;
                }
                mu[i * p] = -mu[i];
            }
        }
        vector<int> coprime(lim + 1, 0);
        for (int d = 1; d <= lim; d++) {
            if (mu[d] == 0 || cntMult[d] == 0) continue;
            for (int m = d; m <= lim; m += d) coprime[m] += mu[d] * cntMult[d];
        }
        int ans = 0;
        for (int v = 1; v <= maxVal; v++) {
            int bad = n - coprime[v];
            int score;
            if (v == 1) score = freq[1] > 0 ? 1 : 0;
            else if (freq[v] > 0) score = v - bad + 1;
            else score = bad > 0 ? v - bad : v - 1;
            ans = max(ans, score);
        }
        vector<int> seen(lim + 1, 0);
        for (int v : nums) {
            if (v <= maxVal || v == 1 || seen[v]) continue;
            seen[v] = 1;
            int bad = n - coprime[v];
            ans = max(ans, v - bad + 1);
        }
        return ans;
    }
};
