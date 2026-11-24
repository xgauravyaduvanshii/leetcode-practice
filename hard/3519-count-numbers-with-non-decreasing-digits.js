// LeetCode 3519. Count Numbers with Non-Decreasing Digits — Hard
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/
// Submission 2202799968 — Accepted, JavaScript
var countNumbers = function(l, r, b) {
    // My thinking: l and r are decimal strings that can be 100
    // digits long, so I convert the bound to base b by repeated
    // decimal-string division, then run a digit DP over those
    // base-b digits: at each position I choose the next digit no
    // smaller than the previous one (leading zeros do not count as
    // started), and the answer is count(r) minus count(l - 1).
    const MOD = 1000000007;
    function divmodStr(s, b) {
        let q = "";
        let rem = 0;
        for (const ch of s) {
            const cur = rem * 10 + (ch.charCodeAt(0) - 48);
            q += String(Math.floor(cur / b));
            rem = cur % b;
        }
        q = q.replace(/^0+/, "") || "0";
        return [q, rem];
    }
    function toBaseB(decStr) {
        if (decStr === "0") return [0];
        const digits = [];
        let s = decStr;
        while (s !== "0") {
            const [q, rem] = divmodStr(s, b);
            s = q;
            digits.push(rem);
        }
        return digits.reverse();
    }
    function decMinusOne(s) {
        const digits = s.split("");
        let i = digits.length - 1;
        while (digits[i] === "0") {
            digits[i] = "9";
            i--;
        }
        digits[i] = String(Number(digits[i]) - 1);
        return digits.join("").replace(/^0+/, "") || "0";
    }
    function countLeq(decStr) {
        const digits = toBaseB(decStr);
        const L = digits.length;
        const memo = new Map();
        function dp(pos, prev, tight, started) {
            if (pos === L) return 1;
            const key = pos + "," + prev + "," + (tight ? 1 : 0) + "," + (started ? 1 : 0);
            if (memo.has(key)) return memo.get(key);
            const limit = tight ? digits[pos] : b - 1;
            let total = 0;
            for (let d = 0; d <= limit; d++) {
                const ntight = tight && d === digits[pos];
                if (!started && d === 0) {
                    total = (total + dp(pos + 1, prev, ntight, false)) % MOD;
                } else if (!started) {
                    total = (total + dp(pos + 1, d, ntight, true)) % MOD;
                } else if (d >= prev) {
                    total = (total + dp(pos + 1, d, ntight, true)) % MOD;
                }
            }
            memo.set(key, total);
            return total;
        }
        return dp(0, 0, true, false);
    }
    let res = countLeq(r);
    if (l !== "0") {
        res = (res - countLeq(decMinusOne(l)) + MOD) % MOD;
    }
    return res;
};
