// LeetCode 1739. Building Boxes — Hard
// https://leetcode.com/problems/building-boxes/
// Submission 2201134486 — Accepted, JavaScript
//
// My thinking: I fill a full pyramid as high as it
// goes, then the leftover boxes form one more partial
// layer — the ground boxes are the pyramid's base plus
// the base of that partial layer.

function minimumBoxes(n) {
    // largest h with h(h+1)(h+2)/6 <= n
    let lo = 0, hi = 1e6;
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (mid * (mid + 1) * (mid + 2) / 6 <= n) lo = mid;
        else hi = mid - 1;
    }
    const h = lo;
    let remaining = n - h * (h + 1) * (h + 2) / 6;
    // largest k with k(k+1)/2 <= remaining
    lo = 0; hi = 1e6;
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (mid * (mid + 1) / 2 <= remaining) lo = mid;
        else hi = mid - 1;
    }
    const k = lo;
    remaining -= k * (k + 1) / 2;
    return h * (h + 1) / 2 + k + (remaining > 0 ? 1 : 0);
}
