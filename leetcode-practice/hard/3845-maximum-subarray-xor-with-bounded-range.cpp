// LeetCode 3845. Maximum Subarray XOR with Bounded Range — Hard
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/
// Submission 2203289713 — Accepted, C++
#include <algorithm>
#include <array>
#include <deque>
#include <vector>
using namespace std;

class Solution {
public:
    int maxXor(vector<int>& nums, int k) {
        // My thinking: the xor of a subarray nums[l..r] is
        // pref[r+1] ^ pref[l], so for each right end r I need
        // the prefix xor in the window that maximises the xor
        // with pref[r+1] — a binary trie over the 15 bits
        // answers that, and it supports deleting a prefix xor
        // when it leaves the window. The window itself is the
        // longest stretch ending at r whose max minus min is
        // at most k: two monotone deques track the min and max
        // while the left edge only moves forward, because
        // shrinking a subarray can only shrink max minus min.
        int n = (int)nums.size();
        vector<int> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] ^ nums[i];
        vector<array<int, 2>> child(1, {-1, -1});
        vector<int> cnt(1, 0);
        auto trieAdd = [&](int x, int delta) {
            int node = 0;
            cnt[node] += delta;
            for (int b = 14; b >= 0; --b) {
                int bit = (x >> b) & 1;
                if (child[node][bit] == -1) {
                    child[node][bit] = (int)child.size();
                    child.push_back({-1, -1});
                    cnt.push_back(0);
                }
                node = child[node][bit];
                cnt[node] += delta;
            }
        };
        auto trieBest = [&](int x) {
            int node = 0, ans = 0;
            for (int b = 14; b >= 0; --b) {
                int bit = (x >> b) & 1;
                int want = bit ^ 1;
                int nxt = child[node][want];
                if (nxt != -1 && cnt[nxt] > 0) {
                    ans |= (1 << b);
                    node = nxt;
                } else {
                    node = child[node][bit];
                }
            }
            return ans;
        };
        trieAdd(pref[0], 1);
        deque<int> minD, maxD;
        int left = 0, ans = 0;
        for (int r = 0; r < n; ++r) {
            while (!maxD.empty() && nums[maxD.back()] <= nums[r]) maxD.pop_back();
            maxD.push_back(r);
            while (!minD.empty() && nums[minD.back()] >= nums[r]) minD.pop_back();
            minD.push_back(r);
            while (nums[maxD.front()] - nums[minD.front()] > k) {
                if (maxD.front() == left) maxD.pop_front();
                if (minD.front() == left) minD.pop_front();
                trieAdd(pref[left], -1);
                ++left;
            }
            if (r > 0) trieAdd(pref[r], 1);
            ans = max(ans, trieBest(pref[r + 1]));
        }
        return ans;
    }
};
