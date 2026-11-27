#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class Solution {
public:
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        // My thinking: the points sitting on you are always
        // seen — for the rest, line up their angles and slide
        // a window as wide as your field of view.
        int lx = location[0], ly = location[1];
        int same = 0;
        vector<double> angles;
        for (auto& p : points) {
            if (p[0] == lx && p[1] == ly) same++;
            else angles.push_back(atan2(p[1] - ly, p[0] - lx) * 180.0 / M_PI);
        }
        sort(angles.begin(), angles.end());
        int n = angles.size();
        for (int i = 0; i < n; i++) angles.push_back(angles[i] + 360.0);
        int best = 0, j = 0;
        for (int i = 0; i < n; i++) {
            while (j < (int)angles.size() && angles[j] - angles[i] <= angle) j++;
            best = max(best, j - i);
        }
        return same + best;
    }
};
