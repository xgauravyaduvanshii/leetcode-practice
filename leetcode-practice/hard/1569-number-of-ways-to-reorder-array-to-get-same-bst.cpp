#include <vector>
using namespace std;

class Solution {
public:
    int numOfWays(vector<int>& nums) {
        // My thinking: the first number is the root and the
        // smaller and larger numbers split left and right —
        // so interleave the two sides' orders in every way.
        const int MOD = 1000000007;
        return (ways(nums) - 1 + MOD) % MOD;
    }

private:
    long long ways(vector<int> arr) {
        const int MOD = 1000000007;
        if (arr.size() <= 2) return 1;
        vector<int> left, right;
        for (int i = 1; i < (int)arr.size(); i++) {
            if (arr[i] < arr[0]) left.push_back(arr[i]);
            else right.push_back(arr[i]);
        }
        long long c = comb(arr.size() - 1, left.size());
        return c * ways(left) % MOD * ways(right) % MOD;
    }

    long long comb(int n, int k) {
        const int MOD = 1000000007;
        long long res = 1;
        if (k > n - k) k = n - k;
        for (int i = 0; i < k; i++) {
            res = res * (n - i) % MOD;
            res = res * modInv(i + 1) % MOD;
        }
        return res;
    }

    long long modPow(long long a, long long e) {
        const int MOD = 1000000007;
        long long res = 1;
        while (e) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    }

    long long modInv(long long a) {
        return modPow(a, 1000000005);
    }
};
