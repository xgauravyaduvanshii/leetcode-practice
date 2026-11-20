#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    string largestNumber(vector<int>& cost, int target) {
        // My thinking: for every cost, keep the longest number
        // reachable — longer beats larger digits — and build
        // each cost up from the cheaper ones.
        vector<string> dp(target + 1, "");
        vector<bool> ok(target + 1, false);
        ok[0] = true;
        for (int t = 1; t <= target; t++) {
            string best = "";
            bool found = false;
            for (int d = 1; d <= 9; d++) {
                int c = cost[d - 1];
                if (t >= c && ok[t - c]) {
                    string cand = dp[t - c] + char('0' + d);
                    if (!found || cand.size() > best.size() || (cand.size() == best.size() && cand > best)) {
                        best = cand;
                        found = true;
                    }
                }
            }
            if (found) {
                dp[t] = best;
                ok[t] = true;
            }
        }
        return ok[target] ? dp[target] : "0";
    }
};
