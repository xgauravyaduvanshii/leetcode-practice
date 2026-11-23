// LeetCode 3003. Maximize the Number of Partitions After Operations — Hard
// https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
// Submission 2201874765 — Accepted, Go
//
// My thinking: I first cut the string
// the greedy way, into the longest
// pieces with at most k different
// letters. Then, for a change at one
// spot, I work out where the first new
// cut falls — the moment the piece
// holds k different letters and the
// changed letter still shows up
// elsewhere — and I count the pieces
// from there on with a table of how
// many pieces the untouched string
// still makes from every position. A
// change at the very start of a piece
// only counts when the fresh letter is
// one the previous piece cannot swallow.

func maxPartitionsAfterOperations(s string, k int) int {
	n := len(s)
	if k == 26 {
		return 1
	}
	// Greedy partition: longest prefixes with at most k distinct letters.
	type segment struct{ l, r int }
	segs := []segment{}
	for i := 0; i < n; {
		seen := map[byte]bool{}
		j := i
		for j < n && (seen[s[j]] || len(seen) < k) {
			seen[s[j]] = true
			j++
		}
		segs = append(segs, segment{i, j - 1})
		i = j
	}
	base := len(segs)
	// nxt[i]: end of the longest prefix starting at i with <= k distinct.
	nxt := make([]int, n)
	cnt := map[byte]int{}
	r := -1
	for i := 0; i < n; i++ {
		if r < i-1 {
			r = i - 1
			cnt = map[byte]int{}
		}
		for r+1 < n && (cnt[s[r+1]] > 0 || len(cnt) < k) {
			r++
			cnt[s[r]]++
		}
		nxt[i] = r
		cnt[s[i]]--
		if cnt[s[i]] == 0 {
			delete(cnt, s[i])
		}
	}
	// dp[i]: pieces the untouched string still makes from i onwards.
	dp := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		dp[i] = 1 + dp[nxt[i]+1]
	}
	// kth[i]: first t >= i with distinct(s[i..t]) == k, or -1.
	kth := make([]int, n)
	cnt = map[byte]int{}
	r = -1
	for i := 0; i < n; i++ {
		if r < i-1 {
			r = i - 1
			cnt = map[byte]int{}
		}
		for r+1 < n && len(cnt) < k {
			r++
			cnt[s[r]]++
		}
		if len(cnt) == k {
			kth[i] = r
		} else {
			kth[i] = -1
		}
		cnt[s[i]]--
		if cnt[s[i]] == 0 {
			delete(cnt, s[i])
		}
	}
	best := base
	for idx, sg := range segs {
		l, rseg := sg.l, sg.r
		distinct := map[byte]bool{}
		for p := l; p <= rseg; p++ {
			distinct[s[p]] = true
		}
		prev := map[byte]bool{}
		if idx > 0 {
			for p := segs[idx-1].l; p <= segs[idx-1].r; p++ {
				prev[s[p]] = true
			}
		}
		// tstar: first spot in the piece where k different letters
		// have shown up; first/second: where each letter occurs.
		tstar := -1
		seen := map[byte]bool{}
		for t := l; t <= rseg; t++ {
			seen[s[t]] = true
			if tstar < 0 && len(seen) == k {
				tstar = t
			}
		}
		if tstar < 0 {
			continue
		}
		first := map[byte]int{}
		second := map[byte]int{}
		for t := l; t <= rseg; t++ {
			ch := s[t]
			if _, ok := first[ch]; !ok {
				first[ch] = t
			} else if _, ok := second[ch]; !ok {
				second[ch] = t
			}
		}
		for p := l; p <= rseg; p++ {
			ch := s[p]
			var v int
			if first[ch] != p {
				v = first[ch]
			} else if s2, ok := second[ch]; ok {
				v = s2
			} else {
				continue // the letter is unique here: no cut at all
			}
			// The first new cut falls where the piece already holds
			// k letters, the change has happened, and the changed
			// letter still shows up somewhere else.
			cutT := tstar
			if p > cutT {
				cutT = p
			}
			if v > cutT {
				cutT = v
			}
			if cutT == p {
				// The piece cuts just before p; the next piece
				// starts at p with the fresh letter.
				w := -1
				if p+1 < n {
					w = kth[p+1]
				}
				var gain int
				if w >= 0 {
					gain = 2 + dp[w] - dp[l]
				} else {
					gain = 2 - dp[l]
				}
				if gain > 0 && base+gain > best {
					best = base + gain
				}
			} else {
				// The piece cuts inside itself at cutT; everything
				// from there on is untouched.
				if p == l {
					union := len(distinct)
					for ch2 := range prev {
						if !distinct[ch2] {
							union++
						}
					}
					if union >= 26 {
						continue
					}
				}
				gain := 1 + dp[cutT] - dp[l]
				if gain > 0 && base+gain > best {
					best = base + gain
				}
			}
		}
	}
	return best
}
