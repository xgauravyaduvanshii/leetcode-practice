// LeetCode 3636. Threshold Majority Queries — Hard
// https://leetcode.com/problems/threshold-majority-queries/
// Submission 2202925094 — Accepted, C++
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> thresholdMajorityQueries(vector<int>& nums,
                                         vector<vector<int>>& queries) {
        // My thinking: the answer to a query is the mode of the
        // range (highest frequency, smallest on a tie) as long as
        // its frequency reaches the threshold, else -1. A range
        // mode is always either the mode of the fully covered
        // middle blocks or one of the elements sitting in the two
        // partial edge blocks, so I precompute the mode of every
        // block pair once and then score only those few candidates
        // per query, counting each one exactly with binary search
        // on its sorted positions list.
        int n = (int)nums.size();
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < n; i++) pos[nums[i]].push_back(i);

        // Split nums into blocks of about sqrt(n).
        int B = max(1, (int)sqrt(n));
        int nb = (n + B - 1) / B;
        auto block_of = [&](int i) { return i / B; };

        // modePair[i][j] = mode (smallest on ties) of blocks i..j.
        vector<vector<int>> modePair(nb, vector<int>(nb, 0));
        for (int i = 0; i < nb; i++) {
            unordered_map<int, int> freq;
            int bestVal = 0, bestFreq = 0;
            for (int j = i; j < nb; j++) {
                for (int k = j * B; k < min((j + 1) * B, n); k++) {
                    int v = nums[k];
                    int c = ++freq[v];
                    if (c > bestFreq || (c == bestFreq && v < bestVal)) {
                        bestFreq = c;
                        bestVal = v;
                    }
                }
                modePair[i][j] = bestVal;
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int l = q[0], r = q[1], threshold = q[2];
            int bl = block_of(l), br = block_of(r);
            if (bl == br) {
                // Tiny range: count directly.
                unordered_map<int, int> freq;
                int bestVal = -1, bestFreq = 0;
                for (int k = l; k <= r; k++) {
                    int v = nums[k];
                    int c = ++freq[v];
                    if (c > bestFreq || (c == bestFreq && v < bestVal)) {
                        bestFreq = c;
                        bestVal = v;
                    }
                }
                ans.push_back(bestFreq >= threshold ? bestVal : -1);
                continue;
            }

            unordered_map<int, bool> seen;
            vector<int> candidates;
            auto addCand = [&](int v) {
                if (!seen[v]) {
                    seen[v] = true;
                    candidates.push_back(v);
                }
            };
            if (bl + 1 <= br - 1) addCand(modePair[bl + 1][br - 1]);
            for (int k = l; k < (bl + 1) * B; k++) addCand(nums[k]);
            for (int k = br * B; k <= r; k++) addCand(nums[k]);

            int bestVal = -1, bestFreq = 0;
            for (int v : candidates) {
                const vector<int>& p = pos[v];
                int c = (int)(upper_bound(p.begin(), p.end(), r) -
                              lower_bound(p.begin(), p.end(), l));
                if (c > bestFreq || (c == bestFreq && v < bestVal)) {
                    bestFreq = c;
                    bestVal = v;
                }
            }
            ans.push_back(bestFreq >= threshold ? bestVal : -1);
        }
        return ans;
    }
};
