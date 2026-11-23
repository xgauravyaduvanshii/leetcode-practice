// LeetCode 2650. Design Cancellable Function — Hard
// https://leetcode.com/problems/design-cancellable-function/
// Submission 2201859323 — Accepted, JavaScript
//
// My thinking: I walk the generator
// step by step, feeding each promise's
// answer back in — and if cancel is
// called I throw "Cancelled" into it
// instead, letting whatever it catches
// decide whether the promise resolves
// or rejects.

/**
 * @param {Generator} generator
 * @return {[Function, Promise]}
 */
var cancellable = function(generator) {
  let cancel;
  const promise = new Promise((resolve, reject) => {
    cancel = () => {
      try {
        const { value, done } = generator.throw("Cancelled");
        if (done) resolve(value);
        else step(value);
      } catch (e) {
        reject(e);
      }
    };
    function step(value) {
      Promise.resolve(value).then(
        (v) => {
          try {
            const { value: next, done } = generator.next(v);
            if (done) resolve(next);
            else step(next);
          } catch (e) {
            reject(e);
          }
        },
        (err) => {
          try {
            const { value: next, done } = generator.throw(err);
            if (done) resolve(next);
            else step(next);
          } catch (e) {
            reject(e);
          }
        }
      );
    }
    try {
      const { value, done } = generator.next();
      if (done) resolve(value);
      else step(value);
    } catch (e) {
      reject(e);
    }
  });
  return [cancel, promise];
};
