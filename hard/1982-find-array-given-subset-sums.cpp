// LeetCode 1982. Find Array Given Subset Sums — Hard
// https://leetcode.com/problems/find-array-given-subset-sums/
// Submission 2201291130 — Accepted, C++
//
// My thinking: the biggest gap between the two
// largest subset sums is the smallest element by
// size, so I peel elements off one at a time —
// a sign only counts if the sums left behind
// still hold 0 and the right ends.

#include <algorithm>
#include <map>
#include <vector>
using namespace std;

class Solution {
    map<int, int> tryRemove(map<int, int> cnt, int a) {
        map<int, int> rest;
        vector<int> keys;
        for (auto &kv : cnt) {
            if (kv.second > 0) keys.push_back(kv.first);
        }
        if (a < 0) reverse(keys.begin(), keys.end());
        for (int s : keys) {
            while (cnt[s] > 0) {
                if (cnt[s + a] <= 0) return map<int, int>();
                cnt[s]--;
                cnt[s + a]--;
                rest[s]++;
            }
        }
        return rest;
    }

public:
    vector<int> recoverArray(int n, vector<int> &sums) {
        map<int, int> cnt;
        for (int s : sums) cnt[s]++;
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            vector<int> keys;
            for (auto &kv : cnt) {
                if (kv.second > 0) keys.push_back(kv.first);
            }
            sort(keys.begin(), keys.end());
            if (keys.size() == 1) {
                // Every subset sum is the same, so the rest are all zeroes.
                while ((int)ans.size() < n) ans.push_back(0);
                break;
            }
            int m = keys[keys.size() - 1] - keys[keys.size() - 2];
            int lo = keys.front(), hi = keys.back();
            map<int, int> rest = tryRemove(cnt, m);
            if (!rest.empty() && rest.count(0) && rest[0] > 0) {
                vector<int> rkeys;
                for (auto &kv : rest) {
                    if (kv.second > 0) rkeys.push_back(kv.first);
                }
                sort(rkeys.begin(), rkeys.end());
                if (!rkeys.empty() && rkeys.front() == lo && rkeys.back() == hi - m) {
                    ans.push_back(m);
                    cnt = rest;
                    continue;
                }
            }
            rest = tryRemove(cnt, -m);
            if (!rest.empty() && rest.count(0) && rest[0] > 0) {
                vector<int> rkeys;
                for (auto &kv : rest) {
                    if (kv.second > 0) rkeys.push_back(kv.first);
                }
                sort(rkeys.begin(), rkeys.end());
                if (!rkeys.empty() && rkeys.front() == lo + m && rkeys.back() == hi) {
                    ans.push_back(-m);
                    cnt = rest;
                    continue;
                }
            }
            // No consistent split; should not happen for valid input.
            break;
        }
        return ans;
    }
};
