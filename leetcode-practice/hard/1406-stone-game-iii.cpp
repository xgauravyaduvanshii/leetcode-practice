#include <vector>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        // My thinking: from each pile, taking one, two or
        // three stones earns their values minus whatever the
        // other player then earns — so work backwards keeping
        // the best difference.
        int n = stoneValue.size();
        vector<int> suffix(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) suffix[i] = suffix[i + 1] + stoneValue[i];
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) {
            int best = INT_MIN;
            for (int k = 1; k <= 3 && i + k <= n; k++) {
                int take = suffix[i] - suffix[i + k];
                best = max(best, take - dp[i + k]);
            }
            dp[i] = best;
        }
        if (dp[0] > 0) return "Alice";
        if (dp[0] < 0) return "Bob";
        return "Tie";
    }
};
