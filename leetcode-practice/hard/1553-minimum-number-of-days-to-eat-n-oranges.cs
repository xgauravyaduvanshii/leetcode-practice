using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<long, long> memo = new Dictionary<long, long>();

    public int MinDays(int n) {
        // My thinking: the big bites need a divisible pile,
        // so eat single oranges just until the pile divides
        // by two or by three, then take the big bite.
        return (int)Dp(n);
    }

    private long Dp(long x) {
        if (x <= 1) return x;
        if (memo.TryGetValue(x, out long cached)) return cached;
        long res = 1 + Math.Min(x % 2 + Dp(x / 2), x % 3 + Dp(x / 3));
        memo[x] = res;
        return res;
    }
}
