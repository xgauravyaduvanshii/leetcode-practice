// 2627. Debounce (Easy)
// https://leetcode.com/problems/debounce/
// Submission 2201031205 -- Accepted, JavaScript
// My thinking: every call cancels the pending timer and
// starts a fresh one, so the function only runs once the
// calls stop for the full wait.
var debounce = function(fn, t) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn(...args), t);
    };
};
