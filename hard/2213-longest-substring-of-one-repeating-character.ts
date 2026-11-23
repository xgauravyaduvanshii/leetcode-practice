// LeetCode 2213. Longest Substring of One Repeating Character — Hard
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/
// Submission 2201625144 — Accepted, TypeScript
//
// My thinking: the string is a row of runs
// of equal letters — each query splits one
// run, drops a single letter in, and lets it
// join its neighbours, while a heap keeps
// the longest run on top.

function longestRepeating(s: string, queryCharacters: string, queryIndices: number[]): number[] {
    const n = s.length;
    const arr = s.split("");
    const segs: [number, number][] = [];
    let i = 0;
    while (i < n) {
        let j = i;
        while (j + 1 < n && arr[j + 1] === arr[i]) j++;
        segs.push([i, j]);
        i = j + 1;
    }
    const cnt = new Map<number, number>();
    const heap: number[] = [];
    const heapPush = (x: number) => {
        heap.push(x);
        let k = heap.length - 1;
        while (k > 0) {
            const p = (k - 1) >> 1;
            if (heap[p] <= heap[k]) break;
            [heap[p], heap[k]] = [heap[k], heap[p]];
            k = p;
        }
    };
    const heapPop = (): number => {
        const top = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let k = 0;
            for (;;) {
                const l = 2 * k + 1, r = 2 * k + 2;
                let smallest = k;
                if (l < heap.length && heap[l] < heap[smallest]) smallest = l;
                if (r < heap.length && heap[r] < heap[smallest]) smallest = r;
                if (smallest === k) break;
                [heap[k], heap[smallest]] = [heap[smallest], heap[k]];
                k = smallest;
            }
        }
        return top;
    };
    const addSeg = (l: number, r: number) => {
        const len = r - l + 1;
        cnt.set(len, (cnt.get(len) ?? 0) + 1);
        heapPush(-len);
    };
    const removeSeg = (l: number, r: number) => {
        const len = r - l + 1;
        cnt.set(len, (cnt.get(len) ?? 0) - 1);
    };
    const currentMax = (): number => {
        while (heap.length > 0 && (cnt.get(-heap[0]) ?? 0) === 0) heapPop();
        return heap.length > 0 ? -heap[0] : 0;
    };
    const findSeg = (idx: number): number => {
        let lo = 0, hi = segs.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (segs[mid][0] <= idx) lo = mid + 1;
            else hi = mid;
        }
        return lo - 1;
    };
    for (let l = 0; l < segs.length; l++) addSeg(segs[l][0], segs[l][1]);
    const ans: number[] = [];
    for (let q = 0; q < queryIndices.length; q++) {
        const idx = queryIndices[q];
        const ch = queryCharacters[q];
        if (arr[idx] !== ch) {
            let pos = findSeg(idx);
            const [l, r] = segs.splice(pos, 1)[0];
            removeSeg(l, r);
            const leftPiece: [number, number] | null = l <= idx - 1 ? [l, idx - 1] : null;
            const rightPiece: [number, number] | null = idx + 1 <= r ? [idx + 1, r] : null;
            arr[idx] = ch;
            let newL = idx, newR = idx;
            if (leftPiece === null && pos > 0 && arr[segs[pos - 1][1]] === ch) {
                const [ll, rr] = segs.splice(pos - 1, 1)[0];
                removeSeg(ll, rr);
                newL = ll;
                pos -= 1;
            }
            if (rightPiece === null && pos < segs.length && arr[segs[pos][0]] === ch) {
                const [ll, rr] = segs.splice(pos, 1)[0];
                removeSeg(ll, rr);
                newR = rr;
            }
            const pieces: [number, number][] = [];
            if (leftPiece !== null) pieces.push(leftPiece);
            pieces.push([newL, newR]);
            if (rightPiece !== null) pieces.push(rightPiece);
            segs.splice(pos, 0, ...pieces);
            for (const [pl, pr] of pieces) addSeg(pl, pr);
        }
        ans.push(currentMax());
    }
    return ans;
}
