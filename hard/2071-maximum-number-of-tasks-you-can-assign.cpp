// LeetCode 2071. Maximum Number of Tasks You Can Assign — Hard
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/
// Submission 2201566158 — Accepted, C++
//
// My thinking: I guess how many tasks I can do
// and check it — the hardest tasks first, each
// one going to the weakest worker who can manage
// it plain, or with a pill if nobody can — and
// I narrow the guess until it just fits.

#include <algorithm>
#include <set>
#include <vector>
using namespace std;

class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        auto can = [&](int k) {
            multiset<int> have(workers.end() - k, workers.end());
            int left = pills;
            for (int t = k - 1; t >= 0; --t) {
                int task = tasks[t];
                auto it = have.lower_bound(task);
                if (it != have.end()) {
                    have.erase(it);
                    continue;
                }
                it = have.lower_bound(task - strength);
                if (it != have.end() && left > 0) {
                    have.erase(it);
                    --left;
                    continue;
                }
                return false;
            }
            return true;
        };
        int lo = 0, hi = min((int)tasks.size(), (int)workers.size());
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
