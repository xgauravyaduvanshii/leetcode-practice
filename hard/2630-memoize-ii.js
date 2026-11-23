// LeetCode 2630. Memoize II — Hard
// https://leetcode.com/problems/memoize-ii/
// Submission 2201856066 — Accepted, JavaScript
//
// My thinking: the same arguments
// should never run the function twice,
// so I file every call down a chain of
// maps — one map per argument — and the
// answer waits at the end of the chain
// for the next identical call.

/**
 * @param {Function} fn
 * @return {Function}
 */
var memoize = function(fn) {
  const root = new Map();
  const RESULT = Symbol("result");
  return function(...args) {
    let node = root;
    for (const arg of args) {
      if (!node.has(arg)) node.set(arg, new Map());
      node = node.get(arg);
    }
    if (!node.has(RESULT)) node.set(RESULT, fn(...args));
    return node.get(RESULT);
  };
};
