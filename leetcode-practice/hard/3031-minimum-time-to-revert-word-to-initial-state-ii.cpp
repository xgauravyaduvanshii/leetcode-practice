// LeetCode 3031. Minimum Time to Revert Word to Initial State II — Hard
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
// Submission 2201904161 — Accepted, C++
//
// My thinking: after t seconds the word
// is its tail from t*k onwards plus any
// t*k letters I choose, so it can match
// the original exactly when that tail
// equals the matching head of the word.
// I find every such shift at once with
// the Z-function, which tells me how
// far the word matches itself at each
// spot, and take the earliest second
// that works (or the one that replaces
// the whole word).

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumTimeToInitialState(string word, int k) {
        int n = word.size();
        // z[i]: longest prefix of word matching word[i:].
        vector<int> z(n, 0);
        int left = 0, right = 0;
        for (int i = 1; i < n; i++) {
            if (i <= right) z[i] = min(right - i + 1, z[i - left]);
            while (i + z[i] < n && word[z[i]] == word[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > right) {
                left = i;
                right = i + z[i] - 1;
            }
        }
        for (int t = 1;; t++) {
            long long s = 1LL * t * k;
            if (s >= n || z[s] >= n - s) return t;
        }
    }
};
