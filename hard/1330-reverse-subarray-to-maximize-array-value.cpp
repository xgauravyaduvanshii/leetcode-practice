#include <vector>
#include <cstdlib>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        // My thinking: reversing a subarray only changes the
        // two adjacencies at its ends — so try every way to
        // rewire an end, plus the best middle swap, which is
        // twice the gap between the biggest small end and the
        // smallest big end of any adjacent pair.
        int n = nums.size();
        int base = 0;
        for (int i = 0; i < n - 1; i++) base += abs(nums[i] - nums[i + 1]);
        int best = base;
        for (int i = 1; i < n; i++) {
            best = max(best, base + abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1]));
            best = max(best, base + abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]));
        }
        int biggestSmall = 0, smallestBig = INT_MAX;
        for (int i = 0; i < n - 1; i++) {
            biggestSmall = max(biggestSmall, min(nums[i], nums[i + 1]));
            smallestBig = min(smallestBig, max(nums[i], nums[i + 1]));
        }
        best = max(best, base + 2 * (biggestSmall - smallestBig));
        return best;
    }
};
