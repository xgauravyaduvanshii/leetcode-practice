// LeetCode 3165. Maximum Sum of Subsequence With Non-adjacent Elements — Hard
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/
// Submission 2202055088 — Accepted, C++
//
// My thinking: each segment keeps a 2x2
// table: the best non-adjacent sum for
// the four combinations of taking or
// skipping its first and last element.
// Merging two segments tries both ways
// across the boundary — the right
// segment's first element can only be
// taken when the left's last is skipped.
// A point update rebuilds the path to
// the root, so each query reads the
// answer off the root.

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    struct Node {
        long long a[2][2];
    };
    const long long NEG = -(1LL << 60);
    Node mergeNode(const Node &L, const Node &R) {
        Node res;
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                res.a[i][j] = max(L.a[i][0] + R.a[0][j], L.a[i][1] + R.a[1][j]);
            }
        }
        return res;
    }
    int maximumSumSubsequence(vector<int>& nums, vector<vector<int>>& queries) {
        const long long MOD = 1000000007LL;
        int n = (int)nums.size();
        int size = 1;
        while (size < n) size <<= 1;
        vector<Node> seg(2 * size);
        Node ident;
        ident.a[0][0] = 0; ident.a[0][1] = NEG;
        ident.a[1][0] = NEG; ident.a[1][1] = 0;
        for (int i = 0; i < 2 * size; i++) seg[i] = ident;
        for (int i = 0; i < n; i++) {
            Node nd;
            nd.a[0][0] = 0; nd.a[0][1] = nums[i];
            nd.a[1][0] = 0; nd.a[1][1] = NEG;
            seg[size + i] = nd;
        }
        for (int i = size - 1; i >= 1; i--) seg[i] = mergeNode(seg[2 * i], seg[2 * i + 1]);
        long long total = 0;
        for (auto &q : queries) {
            int pos = q[0];
            long long x = q[1];
            int p = size + pos;
            seg[p].a[0][0] = 0; seg[p].a[0][1] = x;
            seg[p].a[1][0] = 0; seg[p].a[1][1] = NEG;
            for (p >>= 1; p >= 1; p >>= 1) {
                seg[p] = mergeNode(seg[2 * p], seg[2 * p + 1]);
                if (p == 1) break;
            }
            long long ans = max(seg[1].a[0][0], seg[1].a[0][1]);
            if (ans < 0) ans = 0;
            total += ans;
        }
        return (int)(total % MOD);
    }
};
