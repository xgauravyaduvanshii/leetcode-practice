// 2620. Counter (Easy)
// https://leetcode.com/problems/counter/
// Submission 2200139165 -- Accepted, JavaScript
// My thinking: keep the counter in a closure and hand back the
// current value, then bump it by one for the next call.
var createCounter = function(n) {
    return function() {
        return n++;
    };
};
