#include <vector>
using namespace std;

class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        // My thinking: raising a stretch costs the height of
        // its lowest point — so each step up from the previous
        // height adds exactly that rise to the bill.
        int ops = target[0];
        for (int i = 1; i < (int)target.size(); i++) {
            if (target[i] > target[i - 1]) ops += target[i] - target[i - 1];
        }
        return ops;
    }
};
