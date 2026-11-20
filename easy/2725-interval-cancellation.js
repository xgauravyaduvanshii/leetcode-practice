// 2725. Interval Cancellation (Easy)
// https://leetcode.com/problems/interval-cancellation/
// Submission 2200149355 -- Accepted, JavaScript
// My thinking: run the function once right away, then on a
// timer; the cancel function clears that timer.
var cancellable = function(fn, args, t) {
    fn(...args);
    const timer = setInterval(() => fn(...args), t);
    return function() {
        clearInterval(timer);
    };
};
