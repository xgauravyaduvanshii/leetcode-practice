// LeetCode 1900. The Earliest and Latest Rounds Where Players Compete — Hard
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/
// Submission 2201224606 — Accepted, JavaScript
//
// My thinking: after every round the winners line
// up again by their original numbers, so a round
// is fully described by how many survivors sit
// below, between and above the two stars — they
// meet when the two side counts are equal, and
// every match between other players can swing
// either way, which is what makes the earliest
// and latest rounds differ.

function earliestAndLatest(n, firstPlayer, secondPlayer) {
    const memo = new Map();
    function solve(l, m, r) {
        const key = l + "," + m + "," + r;
        if (memo.has(key)) return memo.get(key);
        let res;
        if (l === r) {
            res = [1, 1];
        } else {
            const k = l + m + r + 2;
            function group(pos) {
                if (pos <= l) return "L";
                if (pos === l + 1) return "F";
                if (pos <= l + m + 1) return "M";
                if (pos === l + m + 2) return "S";
                return "R";
            }
            const c = { LL: 0, MM: 0, RR: 0, LM: 0, LR: 0, MR: 0 };
            let mid = null;
            for (let j = 1; j <= Math.floor(k / 2); j++) {
                const g1 = group(j), g2 = group(k + 1 - j);
                if (g1 === "F" || g2 === "F" || g1 === "S" || g2 === "S") continue;
                const a = g1 < g2 ? g1 : g2, b = g1 < g2 ? g2 : g1;
                c[a + b]++;
            }
            if (k % 2 === 1) mid = group((k + 1) / 2);
            let earliest = Infinity, latest = 0;
            for (let xlm = 0; xlm <= c.LM; xlm++) {
                for (let xlr = 0; xlr <= c.LR; xlr++) {
                    for (let xmr = 0; xmr <= c.MR; xmr++) {
                        const nl = c.LL + xlm + xlr + (mid === "L" ? 1 : 0);
                        const nm = c.MM + (c.LM - xlm) + xmr + (mid === "M" ? 1 : 0);
                        const nr = c.RR + (c.LR - xlr) + (c.MR - xmr) + (mid === "R" ? 1 : 0);
                        const [e, la] = solve(nl, nm, nr);
                        earliest = Math.min(earliest, e + 1);
                        latest = Math.max(latest, la + 1);
                    }
                }
            }
            res = [earliest, latest];
        }
        memo.set(key, res);
        return res;
    }
    return solve(firstPlayer - 1, secondPlayer - firstPlayer - 1, n - secondPlayer);
}
