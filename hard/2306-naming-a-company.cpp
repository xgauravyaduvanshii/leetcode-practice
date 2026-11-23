// LeetCode 2306. Naming a Company — Hard
// https://leetcode.com/problems/naming-a-company/
// Submission 2201672318 — Accepted, C++
//
// My thinking: two names only pair up when
// swapping their first letters makes fresh
// names, so I group the tails by their
// first letter and count the tails each
// group has that the other one lacks.

#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        vector<unordered_set<string>> groups(26);
        for (auto& idea : ideas) {
            groups[idea[0] - 'a'].insert(idea.substr(1));
        }
        long long ans = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = i + 1; j < 26; j++) {
                int common = 0;
                for (auto& s : groups[i]) {
                    if (groups[j].count(s)) common++;
                }
                ans += (long long)(groups[i].size() - common) * (groups[j].size() - common) * 2;
            }
        }
        return ans;
    }
};
