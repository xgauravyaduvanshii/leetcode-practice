// LeetCode 3901. Good Subsequence Queries — Hard
// https://leetcode.com/problems/good-subsequence-queries/
// Submission 2203371663 — Accepted, C#
using System;
using System.Collections.Generic;

public class Solution {
    private const int MaxV = 50000;
    private int[] spf;
    private int[] a;
    private int n;
    private int size;
    private int[] tree;
    private int[] e;
    private Dictionary<int, int> u;
    private Dictionary<int, int> freqd;

    private int Gcd(int x, int y) {
        while (y != 0) {
            int t = x % y;
            x = y;
            y = t;
        }
        return x;
    }

    // Distinct prime factors of x, using the sieve below.
    private List<int> PrimeFactors(int x) {
        List<int> res = new List<int>();
        while (x > 1) {
            int q = spf[x];
            res.Add(q);
            while (x % q == 0) {
                x /= q;
            }
        }
        return res;
    }

    private void PointUpdate(int i, int v) {
        int j = size + i;
        tree[j] = v;
        j /= 2;
        while (j >= 1) {
            tree[j] = Gcd(tree[2 * j], tree[2 * j + 1]);
            j /= 2;
        }
    }

    // First index whose value is not divisible by q, or -1
    // when every value is divisible by q. A prime divides
    // a segment's gcd exactly when it divides every
    // element of the segment, so the search follows the
    // child whose gcd is not divisible by q. Only called
    // while all values are divisible by p.
    private int FindNotDiv(int q) {
        if (tree[1] % q == 0) {
            return -1;
        }
        int j = 1;
        while (j < size) {
            j *= 2;
            if (tree[j] % q == 0) {
                j += 1;
            }
        }
        int idx = j - size;
        return idx < n ? idx : -1;
    }

    // Rebuild the covered set from scratch: a prime
    // dividing all but one element must divide a[0] or
    // a[1], since its unique non-multiple is a single
    // index, so those prime factors are the only
    // candidates.
    private void Rebuild() {
        u.Clear();
        freqd.Clear();
        HashSet<int> cands = new HashSet<int>(PrimeFactors(a[0]));
        cands.UnionWith(PrimeFactors(a[1]));
        foreach (int q in cands) {
            if (e[q] == n - 1) {
                Enter(q, FindNotDiv(q));
            }
        }
    }

    private void Enter(int q, int idx) {
        u[q] = idx;
        freqd[idx] = freqd.ContainsKey(idx) ? freqd[idx] + 1 : 1;
    }

    private void Leave(int q) {
        int idx = u[q];
        u.Remove(q);
        freqd[idx] -= 1;
        if (freqd[idx] == 0) {
            freqd.Remove(idx);
        }
    }

    public int CountGoodSubseq(int[] nums, int p, int[][] queries) {
        // My thinking: a subsequence has gcd exactly p only
        // when every element is divisible by p, so divide
        // those elements by p and ask for gcd exactly 1.
        // Let m be how many elements are divisible by p.
        // When m < n, taking all of them is a good
        // subsequence exactly when their gcd is 1, and no
        // subsequence can have gcd 1 when that gcd is above
        // 1, since the gcd of any subset is a multiple of
        // the gcd of the whole divisible set. When m == n
        // the full array is too long, so we need a proper
        // subsequence with gcd 1 — one exists exactly when
        // some leave-one-out gcd is 1. That fails for every
        // element only when each element is the unique one
        // not divisible by some prime: for a prime q dividing
        // all but one element, that element is "covered".
        // So keep, for every prime q, how many divisible
        // elements it divides (updated from the prime
        // factors of the old and new value only), plus the
        // set of primes dividing all but one element with
        // their unique uncovered index — found with a
        // segment-tree search. The segment tree also
        // carries the gcd of all divisible values (0 stands
        // for not divisible). A query is good when that gcd
        // is 1 and either m < n or not every index is
        // covered.
        n = nums.Length;
        spf = new int[MaxV + 1];
        for (int i = 0; i <= MaxV; i++) {
            spf[i] = i;
        }
        for (int i = 2; i * i <= MaxV; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= MaxV; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        a = new int[n];
        int m = 0;
        for (int i = 0; i < n; i++) {
            a[i] = nums[i] % p == 0 ? nums[i] / p : 0;
            if (a[i] > 0) {
                m++;
            }
        }
        size = 1;
        while (size < n) {
            size *= 2;
        }
        tree = new int[2 * size];
        for (int i = 0; i < n; i++) {
            tree[size + i] = a[i];
        }
        for (int i = size - 1; i >= 1; i--) {
            tree[i] = Gcd(tree[2 * i], tree[2 * i + 1]);
        }

        // e[q]: how many divisible elements are divisible by q.
        e = new int[MaxV + 1];
        foreach (int v in a) {
            if (v > 0) {
                foreach (int q in PrimeFactors(v)) {
                    e[q]++;
                }
            }
        }
        // u[q]: the unique index not divisible by q, for each
        // prime q dividing all but one element (m == n only).
        // freqd[idx]: how many such primes cover idx.
        u = new Dictionary<int, int>();
        freqd = new Dictionary<int, int>();
        if (m == n) {
            Rebuild();
        }

        int ans = 0;
        foreach (int[] query in queries) {
            int ind = query[0];
            int val = query[1];
            int old = a[ind];
            int nw = val % p == 0 ? val / p : 0;
            if (old != nw) {
                bool oldDiv = old > 0;
                bool newDiv = nw > 0;
                PointUpdate(ind, nw);
                a[ind] = nw;
                if (oldDiv && !newDiv) {
                    m--;
                    foreach (int q in PrimeFactors(old)) {
                        e[q]--;
                    }
                    if (m + 1 == n) {
                        u.Clear();
                        freqd.Clear();
                    }
                } else if (newDiv && !oldDiv) {
                    m++;
                    foreach (int q in PrimeFactors(nw)) {
                        e[q]++;
                    }
                    if (m == n) {
                        Rebuild();
                    }
                } else {
                    HashSet<int> oldPrimes = new HashSet<int>(PrimeFactors(old));
                    HashSet<int> newPrimes = new HashSet<int>(PrimeFactors(nw));
                    if (m == n) {
                        foreach (int q in oldPrimes) {
                            if (newPrimes.Contains(q)) {
                                continue;
                            }
                            if (e[q] == n) {
                                Enter(q, ind);
                            } else if (e[q] == n - 1) {
                                Leave(q);
                            }
                            e[q]--;
                        }
                        foreach (int q in newPrimes) {
                            if (oldPrimes.Contains(q)) {
                                continue;
                            }
                            if (e[q] == n - 1) {
                                Leave(q);
                            } else if (e[q] == n - 2) {
                                Enter(q, FindNotDiv(q));
                            }
                            e[q]++;
                        }
                    } else {
                        foreach (int q in oldPrimes) {
                            if (!newPrimes.Contains(q)) {
                                e[q]--;
                            }
                        }
                        foreach (int q in newPrimes) {
                            if (!oldPrimes.Contains(q)) {
                                e[q]++;
                            }
                        }
                    }
                }
            }
            if (m > 0 && tree[1] == 1 && (m < n || freqd.Count < n)) {
                ans++;
            }
        }
        return ans;
    }
}
