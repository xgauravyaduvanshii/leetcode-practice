// LeetCode 2276. Count Integers in Intervals — Hard
// https://leetcode.com/problems/count-integers-in-intervals/
// Submission 2201652126 — Accepted, C++
//
// My thinking: the covered integers are a
// row of disjoint stretches — each new
// interval just swallows every stretch it
// touches and the total is the sum of what
// is left standing.

#include <map>
using namespace std;

class CountIntervals {
public:
    map<int, int> intervals;
    int total = 0;

    CountIntervals() {}

    void add(int left, int right) {
        auto it = intervals.lower_bound(left);
        if (it != intervals.begin()) {
            auto prevIt = prev(it);
            if (prevIt->second >= left - 1) {
                it = prevIt;
            }
        }
        int newL = left, newR = right;
        while (it != intervals.end() && it->first <= newR + 1) {
            newL = min(newL, it->first);
            newR = max(newR, it->second);
            total -= it->second - it->first + 1;
            it = intervals.erase(it);
        }
        intervals[newL] = newR;
        total += newR - newL + 1;
    }

    int count() {
        return total;
    }
};
