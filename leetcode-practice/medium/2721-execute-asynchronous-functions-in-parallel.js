// 2721. Execute Asynchronous Functions in Parallel (Medium)
// https://leetcode.com/problems/execute-asynchronous-functions-in-parallel/
// Submission 2201032386 -- Accepted, JavaScript
// My thinking: I start every function at once and wait
// for all of them — the answers land back in the same
// order the functions were given.
var promiseAll = async function(functions) {
    return Promise.all(functions.map((fn) => fn()));
};
