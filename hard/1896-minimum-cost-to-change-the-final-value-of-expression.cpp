// LeetCode 1896. Minimum Cost to Change the Final Value of Expression — Hard
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
// Submission 2201222043 — Accepted, C++
//
// My thinking: every subexpression carries its
// value and the cheapest price to flip it — a
// digit costs one to flip, and for an operator I
// either flip a child or flip the operator itself
// and one child, whichever is cheaper.

#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string s;
    int i = 0;

    pair<int, int> parseTerm() {
        if (s[i] == '(') {
            i++;
            auto val = parseExpr();
            i++;
            return val;
        }
        int v = s[i] - '0';
        i++;
        return {v, 1};
    }

    pair<int, int> combine(pair<int, int> l, pair<int, int> r, char op) {
        int lv = l.first, lc = l.second;
        int rv = r.first, rc = r.second;
        int val, cost;
        if (op == '&') {
            val = lv & rv;
            if (lv == 1 && rv == 1) cost = min(lc, rc);
            else if (lv == 0 && rv == 0) cost = min(lc + rc, min(lc, rc) + 1);
            else if (lv == 0) cost = min(lc, 1);
            else cost = min(rc, 1);
        } else {
            val = lv | rv;
            if (lv == 0 && rv == 0) cost = min(lc, rc);
            else if (lv == 1 && rv == 1) cost = min(lc + rc, min(lc, rc) + 1);
            else if (lv == 1) cost = min(lc, 1);
            else cost = min(rc, 1);
        }
        return {val, cost};
    }

    pair<int, int> parseExpr() {
        auto left = parseTerm();
        while (i < (int)s.size() && (s[i] == '&' || s[i] == '|')) {
            char op = s[i];
            i++;
            auto right = parseTerm();
            left = combine(left, right, op);
        }
        return left;
    }

    int minOperationsToFlip(string expression) {
        s = expression;
        i = 0;
        auto res = parseExpr();
        return res.second;
    }
};
