// 2715. Timeout Cancellation (Easy)
// https://leetcode.com/problems/timeout-cancellation/
// Submission 2200146887 -- Accepted, JavaScript
// My thinking: set the timer and hand back a function that
// clears it, so calling cancel before the delay stops the call.
var cancellable = function(fn, args, t) {
    const timer = setTimeout(() => fn(...args), t);
    return function() {
        clearTimeout(timer);
    };
};
