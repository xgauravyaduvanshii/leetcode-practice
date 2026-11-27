// LeetCode 4091. Count Magical Substring Pairs II — Hard
// https://leetcode.com/problems/count-magical-substring-pairs-ii/
// Submission 2203709796 — Accepted, C++
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countMagicalPairs(string s) {
        // My thinking: fix the split point j. The left
        // part s[i..j] and the right part s[j+1..k] are
        // magical when they have the same number of
        // distinct characters. As i moves left from j,
        // the distinct count of the left part only grows
        // at the last occurrence of each letter, and as
        // k moves right from j+1, the distinct count of
        // the right part only grows at the first
        // occurrence of each letter. So for each j, sort
        // the last occurrences of all letters to get the
        // lengths L[d] of the i-ranges where the left
        // part has exactly d distinct characters, and
        // precompute (scanning starts from the right)
        // the matching R[j][d] for the k-ranges where
        // the right part has exactly d distinct
        // characters. The answer for this j is the dot
        // product of L and R over d, summed over all j.
        int n = (int)s.size();
        vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = s[i] - 'a';
        vector<array<int, 26>> R(n);
        vector<int> first(26, n);
        for (int start = n - 1; start >= 1; --start) {
            first[a[start]] = start;
            vector<int> q = first;
            sort(q.begin(), q.end());
            q.push_back(n);
            for (int d = 0; d < 26; d++) R[start - 1][d] = q[d + 1] - q[d];
        }
        long long ans = 0;
        vector<int> last(26, -1);
        for (int j = 0; j < n - 1; j++) {
            last[a[j]] = j;
            vector<int> p = last;
            sort(p.begin(), p.end(), greater<int>());
            p.push_back(-1);
            for (int d = 0; d < 26; d++) {
                int L = (p[d] >= 0 ? p[d] - p[d + 1] : 0);
                ans += (long long)L * R[j][d];
            }
        }
        return ans;
    }
};
