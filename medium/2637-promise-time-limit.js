// 2637. Promise Time Limit (Medium)
// https://leetcode.com/problems/promise-time-limit/
// Submission 2201029674 -- Accepted, JavaScript
// My thinking: I race the function against a timer —
// whichever finishes first decides, and a timeout
// rejects with "Time Limit Exceeded".
var timeLimit = function(fn, t) {
    return async function(...args) {
        return Promise.race([
            fn(...args),
            new Promise((_, reject) =>
                setTimeout(() => reject("Time Limit Exceeded"), t)
            ),
        ]);
    };
};
