// 2665. Counter II (Easy)
// https://leetcode.com/problems/counter-ii/
// Submission 2200142583 -- Accepted, JavaScript
// My thinking: keep the count in a closure; increment and
// decrement return the new value, reset restores the initial
// value and returns it.
var createCounter = function(init) {
    let count = init;
    return {
        increment: function() {
            return ++count;
        },
        decrement: function() {
            return --count;
        },
        reset: function() {
            count = init;
            return count;
        }
    };
};
