// LeetCode 3209. Number of Subarrays With AND Value of K — Hard
// https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/
// Submission 2202082334 — Accepted, C++
//
// My thinking: the ANDs of subarrays
// ending at each position are few — AND
// only clears bits, so at most 32
// distinct values survive. I keep that
// small map of value to count, extend it
// with each new element, and add the
// count of subarrays whose AND equals k.

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        long long ans = 0;
        unordered_map<int, long long> prev, cur;
        for (int x : nums) {
            cur.clear();
            cur[x] += 1;
            for (auto& p : prev) {
                cur[p.first & x] += p.second;
            }
            auto it = cur.find(k);
            if (it != cur.end()) ans += it->second;
            prev = cur;
        }
        return ans;
    }
};
