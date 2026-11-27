// LeetCode 3420. Count Non-Decreasing Subarrays After K Operations — Hard
// https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
// Submission 2202520693 — Accepted 731/731, C++
//
// My thinking: to fix a subarray I raise each element to the
// running maximum, so its cost is the sum of the gaps below
// that maximum. I slide a window and keep its cost in `s`: a
// monotonic deque holds the record maxima, so appending a
// value only adds (window max - value). When the cost passes
// k I drop the left end — its record ruled the stretch up to
// its next greater element, and I walk that stretch's own
// records to subtract exactly what they stop costing. Every
// index enters and leaves the deque once, so the pass is linear.
#include <algorithm>
#include <deque>
#include <vector>
using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ng(n, n);
        deque<int> q;
        long long s = 0, ans = 0;
        int j = 0;
        for (int i = 0; i < n; ++i) {
            while (!q.empty() && nums[q.back()] < nums[i]) {
                ng[q.back()] = i;
                q.pop_back();
            }
            q.push_back(i);
            s += (long long)nums[q.front()] - nums[i];
            while (s > k) {
                int old = nums[j];
                int lim = min(i + 1, ng[j]);
                ++j;
                if (!q.empty() && q.front() < j) q.pop_front();
                int c = j;
                while (c < lim) {
                    int nxt = min(lim, ng[c]);
                    s -= (long long)(old - nums[c]) * (nxt - c);
                    c = nxt;
                }
            }
            ans += (long long)(i - j + 1);
        }
        return ans;
    }
};
