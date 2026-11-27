// LeetCode 3013. Divide an Array Into Subarrays With Minimum Cost II — Hard
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/
// Submission 2201884279 — Accepted, TypeScript
//
// My thinking: the first piece always
// costs nums[0], so I only have to pick
// the other k - 1 cut spots. They must
// all sit inside a window of length
// dist, so I slide that window along
// and keep the cheapest k - 1 values in
// it with two heaps — the small ones I
// picked, and the rest waiting to swap
// in.

class MyHeap {
  private data: [number, number][] = [];
  private cmp: (a: [number, number], b: [number, number]) => number;
  constructor(cmp: (a: [number, number], b: [number, number]) => number) {
    this.cmp = cmp;
  }
  size(): number {
    return this.data.length;
  }
  peek(): [number, number] | undefined {
    return this.data[0];
  }
  push(item: [number, number]): void {
    this.data.push(item);
    let i = this.data.length - 1;
    while (i > 0) {
      const p = (i - 1) >> 1;
      if (this.cmp(this.data[i], this.data[p]) < 0) {
        const tmp = this.data[i];
        this.data[i] = this.data[p];
        this.data[p] = tmp;
        i = p;
      } else {
        break;
      }
    }
  }
  pop(): [number, number] | undefined {
    if (this.data.length === 0) return undefined;
    const top = this.data[0];
    const last = this.data.pop() as [number, number];
    if (this.data.length > 0) {
      this.data[0] = last;
      let i = 0;
      for (;;) {
        const l = 2 * i + 1;
        const r = 2 * i + 2;
        let m = i;
        if (l < this.data.length && this.cmp(this.data[l], this.data[m]) < 0) m = l;
        if (r < this.data.length && this.cmp(this.data[r], this.data[m]) < 0) m = r;
        if (m === i) break;
        const tmp = this.data[i];
        this.data[i] = this.data[m];
        this.data[m] = tmp;
        i = m;
      }
    }
    return top;
  }
}

function minimumCost(nums: number[], k: number, dist: number): number {
  const n = nums.length;
  const need = k - 1;
  // small: max-heap of the `need` cheapest live values in the window,
  // with their running sum. large: min-heap of the rest.
  const small = new MyHeap((a, b) => b[0] - a[0]);
  const large = new MyHeap((a, b) => a[0] - b[0]);
  const inSmall: boolean[] = new Array(n).fill(false);
  const alive: boolean[] = new Array(n).fill(false);
  let smallSum = 0;
  let smallCnt = 0;
  let largeCnt = 0;

  const clean = (heap: MyHeap, wantSmall: boolean): boolean => {
    while (heap.size() > 0) {
      const top = heap.peek() as [number, number];
      if (!alive[top[1]] || inSmall[top[1]] !== wantSmall) {
        heap.pop();
      } else {
        return true;
      }
    }
    return false;
  };
  const rebalance = (): void => {
    clean(small, true);
    clean(large, false);
    while (smallCnt < need && largeCnt > 0) {
      if (!clean(large, false)) break;
      const top = large.pop() as [number, number];
      largeCnt--;
      inSmall[top[1]] = true;
      smallSum += top[0];
      smallCnt++;
      small.push(top);
    }
    while (smallCnt > need) {
      if (!clean(small, true)) break;
      const top = small.pop() as [number, number];
      smallSum -= top[0];
      smallCnt--;
      inSmall[top[1]] = false;
      large.push(top);
      largeCnt++;
    }
    // The biggest picked value must not beat the smallest unpicked.
    while (clean(small, true) && clean(large, false)) {
      const sTop = small.peek() as [number, number];
      const lTop = large.peek() as [number, number];
      if (sTop[0] > lTop[0]) {
        small.pop();
        large.pop();
        smallSum += lTop[0] - sTop[0];
        inSmall[sTop[1]] = false;
        inSmall[lTop[1]] = true;
        small.push(lTop);
        large.push(sTop);
      } else {
        break;
      }
    }
  };

  let ans: number | null = null;
  // Window [L, R] with R = min(L + dist, n - 1); cuts are indices 1..n-1.
  for (let left = 1; left < n; left++) {
    const right = Math.min(left + dist, n - 1);
    if (left === 1) {
      for (let idx = 1; idx <= right; idx++) {
        alive[idx] = true;
        large.push([nums[idx], idx]);
        largeCnt++;
      }
    } else {
      const out = left - 1;
      if (alive[out]) {
        alive[out] = false;
        if (inSmall[out]) {
          inSmall[out] = false;
          smallSum -= nums[out];
          smallCnt--;
        } else {
          largeCnt--;
        }
      }
      const prevRight = Math.min(left - 1 + dist, n - 1);
      if (right > prevRight) {
        alive[right] = true;
        large.push([nums[right], right]);
        largeCnt++;
      }
    }
    rebalance();
    if (smallCnt === need) {
      const total = nums[0] + smallSum;
      if (ans === null || total < ans) ans = total;
    }
  }
  return ans === null ? nums[0] : ans;
}
