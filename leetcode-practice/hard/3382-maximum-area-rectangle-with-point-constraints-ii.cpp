// LeetCode 3382. Maximum Area Rectangle With Point Constraints II — Hard
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/
// Submission 2202495055 — Accepted 594/594, C++
//
// My thinking: a valid rectangle's two y's must be neighbours in both of
// its columns, otherwise a point of that column would sit on its edge, and
// its two columns must be consecutive occurrences of that y-pair, otherwise
// a point would sit on its top or bottom edge. So I sweep the columns left
// to right, remember the last column of each neighbouring y-pair, and keep
// a segment tree of the last column seen for every y: a candidate is empty
// exactly when no y between its sides was seen after its left column.
class Solution {
public:
    long long maxArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        vector<pair<int, int>> pts(n);
        for (int i = 0; i < n; i++) pts[i] = {xCoord[i], yCoord[i]};
        sort(pts.begin(), pts.end());
        vector<int> allY;
        for (auto& p : pts) allY.push_back(p.second);
        sort(allY.begin(), allY.end());
        allY.erase(unique(allY.begin(), allY.end()), allY.end());
        int m = allY.size();
        int size = 1;
        while (size < m) size *= 2;
        vector<int> tree(2 * size, -1);
        auto update = [&](int i, int v) {
            int j = i + size;
            tree[j] = v;
            for (j /= 2; j; j /= 2)
                tree[j] = max(tree[2 * j], tree[2 * j + 1]);
        };
        auto query = [&](int l, int r) {
            int best = -1;
            l += size;
            r += size;
            while (l <= r) {
                if (l % 2 == 1) best = max(best, tree[l++]);
                if (r % 2 == 0) best = max(best, tree[r--]);
                l /= 2;
                r /= 2;
            }
            return best;
        };
        auto yid = [&](int y) {
            return (int)(lower_bound(allY.begin(), allY.end(), y) - allY.begin());
        };
        map<pair<int, int>, int> pairLast;
        long long ans = -1;
        for (int i = 0; i < n;) {
            int x = pts[i].first;
            int j = i;
            while (j < n && pts[j].first == x) j++;
            vector<int> ys;
            for (int k = i; k < j; k++) ys.push_back(pts[k].second);
            sort(ys.begin(), ys.end());
            for (int k = 0; k + 1 < (int)ys.size(); k++) {
                auto key = make_pair(ys[k], ys[k + 1]);
                auto it = pairLast.find(key);
                if (it != pairLast.end()) {
                    int xp = it->second;
                    if (query(yid(ys[k]), yid(ys[k + 1])) <= xp)
                        ans = max(ans, (long long)(x - xp) * (ys[k + 1] - ys[k]));
                }
            }
            for (int y : ys) update(yid(y), x);
            for (int k = 0; k + 1 < (int)ys.size(); k++)
                pairLast[{ys[k], ys[k + 1]}] = x;
            i = j;
        }
        return ans;
    }
};
