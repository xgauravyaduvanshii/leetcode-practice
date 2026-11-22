// LeetCode 1851. Minimum Interval to Include Each Query — Hard
// https://leetcode.com/problems/minimum-interval-to-include-each-query/
// Submission 2201202341 — Accepted, C++
//
// My thinking: I sort the intervals by their left
// end and sweep the queries in order, keeping the
// intervals that have started in a heap by size
// and dropping the ones that already ended — the
// smallest one left is the answer.

#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end());
        vector<int> order(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) order[i] = i;
        sort(order.begin(), order.end(), [&](int a, int b) { return queries[a] < queries[b]; });
        vector<int> ans(queries.size(), -1);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;
        size_t j = 0;
        for (int qi : order) {
            int q = queries[qi];
            while (j < intervals.size() && intervals[j][0] <= q) {
                heap.push({intervals[j][1] - intervals[j][0] + 1, intervals[j][1]});
                j++;
            }
            while (!heap.empty() && heap.top().second < q) heap.pop();
            if (!heap.empty()) ans[qi] = heap.top().first;
        }
        return ans;
    }
};
