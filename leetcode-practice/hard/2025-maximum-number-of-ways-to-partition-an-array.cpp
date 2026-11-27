// LeetCode 2025. Maximum Number of Ways to Partition an Array — Hard
// https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/
// Submission 2201553157 — Accepted, C++
//
// My thinking: changing one number only moves
// the total and the prefix sums by the same
// gap, so for each spot I ask how many splits
// land exactly on half — with and without the
// change — and keep the best count.

#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> prefix(n);
        long long s = 0;
        for (int i = 0; i < n; ++i) {
            s += nums[i];
            prefix[i] = s;
        }
        long long total = s;
        int ans = 0;
        if (total % 2 == 0) {
            for (int i = 0; i < n - 1; ++i) {
                if (prefix[i] == total / 2) ++ans;
            }
        }
        unordered_map<long long, int> rightFreq;
        for (int i = 0; i < n - 1; ++i) ++rightFreq[prefix[i]];
        unordered_map<long long, int> leftFreq;
        for (int j = 0; j < n; ++j) {
            long long delta = (long long)k - nums[j];
            int count = 0;
            long long t1 = total + delta;
            if (t1 % 2 == 0) {
                auto it = leftFreq.find(t1 / 2);
                if (it != leftFreq.end()) count += it->second;
            }
            long long t2 = total - delta;
            if (t2 % 2 == 0) {
                auto it = rightFreq.find(t2 / 2);
                if (it != rightFreq.end()) count += it->second;
            }
            ans = max(ans, count);
            if (j < n - 1) {
                if (--rightFreq[prefix[j]] == 0) rightFreq.erase(prefix[j]);
                ++leftFreq[prefix[j]];
            }
        }
        return ans;
    }
};
