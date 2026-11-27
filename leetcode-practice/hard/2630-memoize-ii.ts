// LeetCode 2630. Memoize II — Hard
// https://leetcode.com/problems/memoize-ii/
// Submission 2201856690 — Accepted, TypeScript
//
// My thinking: the same arguments
// should never run the function twice,
// so I file every call down a chain of
// maps — one map per argument — and the
// answer waits at the end of the chain
// for the next identical call.

type Fn = (...args: any[]) => any;

function memoize(fn: Fn): Fn {
  const root = new Map<any, any>();
  const RESULT = Symbol("result");
  return function (...args: any[]): any {
    let node: Map<any, any> = root;
    for (const arg of args) {
      if (!node.has(arg)) node.set(arg, new Map());
      node = node.get(arg);
    }
    if (!node.has(RESULT)) node.set(RESULT, fn(...args));
    return node.get(RESULT);
  };
}
