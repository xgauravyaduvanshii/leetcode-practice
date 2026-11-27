// 2666. Allow One Function Call (Easy)
// https://leetcode.com/problems/allow-one-function-call/
// Submission 2200143107 -- Accepted, JavaScript
// My thinking: remember whether the function has run; the first
// call runs it and returns its result, every later call returns
// undefined without touching it again.
var once = function(fn) {
    let called = false;
    return function(...args) {
        if (called) {
            return undefined;
        }
        called = true;
        return fn(...args);
    };
};
