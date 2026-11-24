// LeetCode 3435. Frequencies of Shortest Supersequences — Hard
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/
// Submission 2202533063 — Accepted 808/808, TypeScript
//
// My thinking: a shortest supersequence uses each letter
// once, except some letters twice. Take the order of
// first appearances: a letter must be doubled exactly
// when some word points into it from a letter that first
// appears later (or the word is a double like "aa").
// So I pick the first-appearance order that doubles the
// fewest letters — a DP over subsets of the at most 16
// letters — then collect every doubled set any cheapest
// order produces, and report each as a frequency array.
function supersequences(words: string[]): number[][] {
    const letters = [...new Set(words.join(""))].sort();
    const m = letters.length;
    const idx = new Map<string, number>(letters.map((ch, i) => [ch, i]));
    const inMask: number[] = new Array(m).fill(0);
    const selfLoop: boolean[] = new Array(m).fill(false);
    for (const w of words) {
        const a = idx.get(w[0])!;
        const b = idx.get(w[1])!;
        if (a === b) {
            selfLoop[a] = true;
        } else {
            inMask[b] |= 1 << a;
        }
    }
    const full = (1 << m) - 1;
    const INF = 1e9;
    // h[S] = fewest doubled letters needed to place the set
    // S, given the letters outside S are already placed.
    const h: number[] = new Array(1 << m).fill(INF);
    h[0] = 0;
    for (let S = 1; S <= full; S++) {
        const placed = full ^ S;
        let best = INF;
        for (let v = 0; v < m; v++) {
            if ((S & (1 << v)) === 0) continue;
            const bad = selfLoop[v] || (inMask[v] & ~placed) !== 0 ? 1 : 0;
            best = Math.min(best, bad + h[S ^ (1 << v)]);
        }
        h[S] = best;
    }
    // g[S] = doubled-letter masks achievable by a cheapest
    // ordering of the set S.
    const memo = new Map<number, Set<number>>();
    const g = (S: number): Set<number> => {
        if (S === 0) return new Set([0]);
        const hit = memo.get(S);
        if (hit) return hit;
        const placed = full ^ S;
        const out = new Set<number>();
        for (let v = 0; v < m; v++) {
            if ((S & (1 << v)) === 0) continue;
            const bad = selfLoop[v] || (inMask[v] & ~placed) !== 0 ? 1 : 0;
            if (bad + h[S ^ (1 << v)] === h[S]) {
                for (const r of g(S ^ (1 << v))) {
                    out.add(r | (bad ? 1 << v : 0));
                }
            }
        }
        memo.set(S, out);
        return out;
    };
    const ans: number[][] = [];
    for (const rmask of g(full)) {
        const freq: number[] = new Array(26).fill(0);
        for (let i = 0; i < m; i++) {
            freq[letters[i].charCodeAt(0) - 97] = ((rmask >> i) & 1) ? 2 : 1;
        }
        ans.push(freq);
    }
    return ans;
}
