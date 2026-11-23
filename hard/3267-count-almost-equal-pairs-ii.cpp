// LeetCode 3267. Count Almost Equal Pairs II — Hard
// https://leetcode.com/problems/count-almost-equal-pairs-ii/
// Submission 2202170290 — Accepted, C++
//
// My thinking: two numbers can only become
// equal if their non-zero digits match, so I
// group numbers by their sorted non-zero digits.
// Inside a group, every number reaches only a
// handful of values with at most two digit swaps
// (leading zeros allowed), so I generate those
// values and count the matching pairs, counting
// each pair once by value order.

class Solution {
public:
    int countPairs(vector<int>& nums) {
        unordered_map<int, int> freq;
        for (int x : nums) freq[x]++;
        vector<int> vals;
        for (auto &p : freq) vals.push_back(p.first);
        unordered_map<int, int> length;
        for (int v : vals) length[v] = (int)to_string(v).size();
        map<string, vector<int>> groups;
        for (int v : vals) {
            string s = to_string(v), sig;
            for (char c : s) if (c != '0') sig += c;
            sort(sig.begin(), sig.end());
            groups[sig].push_back(v);
        }
        long long ans = 0;
        for (auto &p : freq) ans += 1LL * p.second * (p.second - 1) / 2;
        for (auto &gp : groups) {
            auto &group = gp.second;
            if (group.size() < 2) continue;
            unordered_set<int> groupSet(group.begin(), group.end());
            for (int v : group) {
                string s = to_string(v);
                int L = (int)s.size();
                vector<string> first;
                first.push_back(s);
                for (int i = 0; i < L; i++)
                    for (int j = i + 1; j < L; j++)
                        if (s[i] != s[j]) {
                            string t = s;
                            swap(t[i], t[j]);
                            first.push_back(t);
                        }
                unordered_set<int> v2;
                for (string t : first) {
                    v2.insert(stoi(t));
                    for (int i = 0; i < L; i++)
                        for (int j = i + 1; j < L; j++)
                            if (t[i] != t[j]) {
                                string u = t;
                                swap(u[i], u[j]);
                                v2.insert(stoi(u));
                            }
                }
                for (int w : v2) {
                    if (!groupSet.count(w) || w == v) continue;
                    if (length[w] < L) ans += 1LL * freq[v] * freq[w];
                    else if (length[w] == L && w > v) ans += 1LL * freq[v] * freq[w];
                }
            }
        }
        return (int)ans;
    }
};
