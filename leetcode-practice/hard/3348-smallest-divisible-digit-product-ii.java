// LeetCode 3348. Smallest Divisible Digit Product II — Hard
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/
// Submission 2202407607 — Accepted, Java
//
// My thinking: a digit product only involves the primes 2, 3, 5, 7, so if t
// has any other prime factor the answer is -1. Otherwise I factor t into the
// exponents it needs, and a memoised DP gives the fewest digits covering any
// remaining exponents. For the same length I keep the longest possible prefix
// of num and raise the rightmost digit I can, filling the rest with the
// smallest feasible digits. If that fails I use a longer length, where the
// fewest digits (lexicographically smallest, padded with 1s) is optimal —
// more 1s up front always beats any other multiset of the same length.
class Solution {
    // digit exponent contributions for 2..9 over primes (2, 3, 5, 7)
    private static final int[][] CONTRIB = {
        {1, 0, 0, 0}, {0, 1, 0, 0}, {2, 0, 0, 0}, {0, 0, 1, 0},
        {1, 1, 0, 0}, {0, 0, 0, 1}, {3, 0, 0, 0}, {0, 2, 0, 0}
    };
    private int[][][][] memo;

    public String smallestDivisibleDigitProduct(String num, long t) {
        int[] need = new int[4];
        long x = t;
        int[] primes = {2, 3, 5, 7};
        for (int i = 0; i < 4; i++) {
            while (x % primes[i] == 0) {
                need[i]++;
                x /= primes[i];
            }
        }
        if (x != 1) {
            return "-1";
        }
        memo = new int[need[0] + 1][need[1] + 1][need[2] + 1][need[3] + 1];
        for (int a = 0; a <= need[0]; a++) {
            for (int b = 0; b <= need[1]; b++) {
                for (int c = 0; c <= need[2]; c++) {
                    java.util.Arrays.fill(memo[a][b][c], -1);
                }
            }
        }
        int n = num.length();
        int[] digits = new int[n];
        for (int i = 0; i < n; i++) {
            digits[i] = num.charAt(i) - '0';
        }
        // prefix exponent sums (clipped at need) and prefix zero counts
        int[][] pref = new int[n + 1][4];
        int[] prefZero = new int[n + 1];
        for (int i = 0; i < n; i++) {
            System.arraycopy(pref[i], 0, pref[i + 1], 0, 4);
            int dg = digits[i];
            if (dg >= 2) {
                int[] co = CONTRIB[dg - 2];
                for (int j = 0; j < 4; j++) {
                    pref[i + 1][j] = Math.min(need[j], pref[i + 1][j] + co[j]);
                }
            }
            prefZero[i + 1] = prefZero[i] + (dg == 0 ? 1 : 0);
        }
        boolean numOk = prefZero[n] == 0;
        for (int j = 0; j < 4 && numOk; j++) {
            if (pref[n][j] != need[j]) {
                numOk = false;
            }
        }
        if (numOk) {
            return num;
        }
        // same-length search: split at i, rightmost first
        for (int i = n - 1; i >= 0; i--) {
            if (prefZero[i] != 0) {
                continue;
            }
            for (int d = digits[i] + 1; d <= 9; d++) {
                int[] rem = new int[4];
                for (int j = 0; j < 4; j++) {
                    rem[j] = need[j] - pref[i][j];
                }
                rem = subtract(rem, d);
                int r = n - 1 - i;
                if (minDigits(rem[0], rem[1], rem[2], rem[3]) > r) {
                    continue;
                }
                StringBuilder out = new StringBuilder();
                for (int j = 0; j < i; j++) {
                    out.append((char) ('0' + digits[j]));
                }
                out.append((char) ('0' + d));
                int[] state = rem;
                for (int pos = i + 1; pos < n; pos++) {
                    int left = n - 1 - pos;
                    for (int dd = 1; dd <= 9; dd++) {
                        int[] ns = subtract(state, dd);
                        if (minDigits(ns[0], ns[1], ns[2], ns[3]) <= left) {
                            out.append((char) ('0' + dd));
                            state = ns;
                            break;
                        }
                    }
                }
                return out.toString();
            }
        }
        // longer length: fewest digits, lexicographically smallest
        int m = minDigits(need[0], need[1], need[2], need[3]);
        int[] state = need.clone();
        java.util.ArrayList<Integer> chosen = new java.util.ArrayList<>();
        int prev = 2;
        while (state[0] != 0 || state[1] != 0 || state[2] != 0 || state[3] != 0) {
            int cur = minDigits(state[0], state[1], state[2], state[3]);
            for (int d = prev; d <= 9; d++) {
                int[] ns = subtract(state, d);
                if (minDigits(ns[0], ns[1], ns[2], ns[3]) == cur - 1) {
                    chosen.add(d);
                    state = ns;
                    prev = d;
                    break;
                }
            }
        }
        int length = Math.max(n + 1, m);
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < length - chosen.size(); i++) {
            ans.append('1');
        }
        for (int d : chosen) {
            ans.append((char) ('0' + d));
        }
        return ans.toString();
    }

    private int[] subtract(int[] state, int digit) {
        if (digit == 1) {
            return state.clone();
        }
        int[] co = CONTRIB[digit - 2];
        int[] ns = new int[4];
        for (int j = 0; j < 4; j++) {
            ns[j] = Math.max(0, state[j] - co[j]);
        }
        return ns;
    }

    private int minDigits(int a, int b, int c, int d) {
        if (a == 0 && b == 0 && c == 0 && d == 0) {
            return 0;
        }
        if (memo[a][b][c][d] != -1) {
            return memo[a][b][c][d];
        }
        int best = Integer.MAX_VALUE / 2;
        for (int i = 0; i < 8; i++) {
            int da = CONTRIB[i][0], db = CONTRIB[i][1];
            int dc = CONTRIB[i][2], dd = CONTRIB[i][3];
            // a digit that covers nothing still needed is useless here
            // (and would recurse on the same state forever)
            if ((da > 0 && a > 0) || (db > 0 && b > 0)
                    || (dc > 0 && c > 0) || (dd > 0 && d > 0)) {
                int v = 1 + minDigits(Math.max(0, a - da), Math.max(0, b - db),
                        Math.max(0, c - dc), Math.max(0, d - dd));
                best = Math.min(best, v);
            }
        }
        memo[a][b][c][d] = best;
        return best;
    }
}
