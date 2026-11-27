// LeetCode 3351. Sum of Good Subsequences — Hard
// https://leetcode.com/problems/sum-of-good-subsequences/
// Submission 2202412714 — Accepted, C++
//
// My thinking: for each value v I keep the count of good subsequences
// ending in v and the sum of their elements. A new element x starts the
// singleton [x] and extends every good subsequence ending in x-1 or x+1,
// adding x to each extended sum. Neighbours differ from x, so updating x
// never interferes with the neighbours I just read.
class Solution {
public:
    int sumOfGoodSubsequences(vector<int>& nums) {
        const int MOD = 1000000007;
        unordered_map<int, long long> cnt, sum;
        long long ans = 0;
        for (int x : nums) {
            long long c = 1, s = x;
            for (int y : {x - 1, x + 1}) {
                auto it = cnt.find(y);
                if (it != cnt.end()) {
                    c = (c + it->second) % MOD;
                    s = (s + sum[y] + (long long)x * it->second) % MOD;
                }
            }
            cnt[x] = (cnt[x] + c) % MOD;
            sum[x] = (sum[x] + s) % MOD;
            ans = (ans + s) % MOD;
        }
        return (int)ans;
    }
};
