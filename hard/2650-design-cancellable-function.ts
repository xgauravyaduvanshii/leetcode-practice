// LeetCode 2650. Design Cancellable Function — Hard
// https://leetcode.com/problems/design-cancellable-function/
// Submission 2201860592 — Accepted, TypeScript
//
// My thinking: I walk the generator
// step by step, feeding each promise's
// answer back in — and if cancel is
// called I throw "Cancelled" into it
// instead, letting whatever it catches
// decide whether the promise resolves
// or rejects.

function cancellable<T>(generator: Generator<Promise<any>, T, any>): [() => void, Promise<T>] {
  let cancel: () => void;
  const promise = new Promise<T>((resolve, reject) => {
    cancel = () => {
      try {
        const { value, done } = generator.throw("Cancelled");
        if (done) resolve(value);
        else step(value);
      } catch (e) {
        reject(e);
      }
    };
    function step(value: any): void {
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
  return [cancel!, promise];
}
