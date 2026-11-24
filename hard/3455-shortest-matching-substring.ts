// LeetCode 3455. Shortest Matching Substring — Hard
// https://leetcode.com/problems/shortest-matching-substring/
// Submission 2202552666 — Accepted 795/795, TypeScript
function shortestMatchingSubstring(s: string, p: string): number {
    // My thinking: the two stars split p into three literals
    // a, b, c, so a match is an a-occurrence followed by the
    // earliest later b-occurrence and then the earliest later
    // c-occurrence. I list every occurrence of each literal
    // with KMP (repeated indexOf is too slow on long runs of
    // the same letter), then sweep the a-starts with two
    // pointers that only move forward, and keep the shortest
    // span from an a-start to the end of its c.
    const n = s.length;

    function starts(pat: string): number[] {
        if (pat.length === 0) {
            const all: number[] = [];
            for (let i = 0; i <= n; i++) all.push(i);
            return all;
        }
        const m = pat.length;
        const lps: number[] = new Array(m).fill(0);
        let length = 0;
        let i = 1;
        while (i < m) {
            if (pat[i] === pat[length]) {
                length++;
                lps[i] = length;
                i++;
            } else if (length > 0) {
                length = lps[length - 1];
            } else {
                i++;
            }
        }
        const res: number[] = [];
        i = 0;
        let j = 0;
        while (i < n) {
            if (s[i] === pat[j]) {
                i++;
                j++;
            }
            if (j === m) {
                res.push(i - j);
                j = lps[j - 1];
            } else if (i < n && s[i] !== pat[j]) {
                if (j > 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return res;
    }

    const [a, b, c] = p.split("*");
    const A = starts(a);
    const B = starts(b);
    const C = starts(c);
    const la = a.length;
    const lb = b.length;
    const lc = c.length;
    let ans = n + 1;
    let j = 0;
    let k = 0;
    for (const i of A) {
        while (j < B.length && B[j] < i + la) j++;
        if (j === B.length) break;
        while (k < C.length && C[k] < B[j] + lb) k++;
        if (k === C.length) break;
        ans = Math.min(ans, C[k] + lc - i);
    }
    return ans > n ? -1 : ans;
}
