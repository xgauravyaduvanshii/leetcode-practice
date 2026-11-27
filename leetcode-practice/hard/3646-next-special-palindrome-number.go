// LeetCode 3646. Next Special Palindrome Number — Hard
// https://leetcode.com/problems/next-special-palindrome-number/
// Submission 2202929130 — Accepted, Go
import (
	"strconv"
	"strings"
)

func nextSpecialPalindrome(n int64) int64 {
	// My thinking: a special number never contains 0 (0 would
	// have to appear exactly 0 times) and a digit d appears
	// exactly d times, so the digit set is a subset of 1..9
	// with at most one odd digit (a palindrome can have only
	// one digit with an odd count). There are only 96 such
	// subsets, so I try each one: its length is fixed, its
	// palindrome is fixed by its left half, and for the length
	// matching n I build the smallest half that beats n digit
	// by digit, preferring to stay equal to n while a valid
	// completion still exists, and otherwise taking the
	// smallest larger digit. The answer is the smallest
	// candidate over all subsets.
	s := strconv.FormatInt(n, 10)
	digits := len(s)
	var best int64 = -1

	smallestPalindrome := func(half []int, middle int) int64 {
		var b strings.Builder
		for _, d := range half {
			b.WriteByte(byte('0' + d))
		}
		if middle >= 0 {
			b.WriteByte(byte('0' + middle))
		}
		for i := len(half) - 1; i >= 0; i-- {
			b.WriteByte(byte('0' + half[i]))
		}
		v, _ := strconv.ParseInt(b.String(), 10, 64)
		return v
	}

	// suffixCanBeat reports whether the remaining half digits
	// can fill the half positions so the half beats tgtHalf,
	// or equals it with the middle digit beating midT
	// (midT < 0 means the length is even, no middle digit).
	suffixCanBeat := func(rem [10]int, tgtHalf string, midT int, middle int) bool {
		counts := rem
		for i := 0; i < len(tgtHalf); i++ {
			t := int(tgtHalf[i] - '0')
			for d := t + 1; d <= 9; d++ {
				if counts[d] > 0 {
					return true
				}
			}
			if counts[t] == 0 {
				return false
			}
			counts[t]--
		}
		if midT < 0 {
			return false
		}
		return middle > midT
	}

	// smallestHalfAbove finds the smallest palindrome of this
	// digit set that is > s, or -1. The palindrome is fixed by
	// its first half t (length m); t > s[:m] already means the
	// palindrome beats s, while t == s[:m] needs the mirrored
	// half to beat s[m:].
	smallestHalfAbove := func(halfCounts [10]int, middle, L int) int64 {
		m := (L + 1) / 2
		odd := L%2 == 1
		rem := halfCounts
		t := make([]int, 0, m)
		for pos := 0; pos < m; pos++ {
			var cands []int
			if odd && pos == m-1 {
				cands = []int{middle}
			} else {
				for d := 1; d <= 9; d++ {
					if rem[d] > 0 {
						cands = append(cands, d)
					}
				}
			}
			placed := false
			for _, c := range cands {
				if c < int(s[pos]-'0') {
					continue
				}
				if c > int(s[pos]-'0') {
					// A larger digit here already beats s:
					// finish with the smallest arrangement.
					r2 := rem
					if !(odd && pos == m-1) {
						r2[c]--
					}
					tt := append(append([]int{}, t...), c)
					for d := 1; d <= 9; d++ {
						for k := 0; k < r2[d]; k++ {
							tt = append(tt, d)
						}
					}
					if odd && len(tt) == m-1 {
						tt = append(tt, middle)
					}
					var b strings.Builder
					for _, d := range tt {
						b.WriteByte(byte('0' + d))
					}
					leftLen := m
					if odd {
						leftLen = m - 1
					}
					for i := leftLen - 1; i >= 0; i-- {
						b.WriteByte(byte('0' + tt[i]))
					}
					v, _ := strconv.ParseInt(b.String(), 10, 64)
					return v
				}
				// c equals s[pos]: stay equal if a completion
				// can still beat s.
				r2 := rem
				if !(odd && pos == m-1) {
					r2[c]--
				}
				var tgtHalf string
				midT := -1
				if odd {
					if pos < m-1 {
						tgtHalf = s[pos+1 : m-1]
					}
					midT = int(s[m-1] - '0')
				} else {
					tgtHalf = s[pos+1 : m]
				}
				if suffixCanBeat(r2, tgtHalf, midT, middle) {
					t = append(t, c)
					rem = r2
					placed = true
					break
				}
				// The only equal completion is tgtHalf itself
				// (plus the middle): check its mirror.
				var cnt [10]int
				for i := 0; i < len(tgtHalf); i++ {
					cnt[int(tgtHalf[i]-'0')]++
				}
				equal := true
				for d := 1; d <= 9; d++ {
					if r2[d] != cnt[d] {
						equal = false
						break
					}
				}
				if equal && (midT < 0 || middle == midT) {
					tFull := append(append([]int{}, t...), c)
					for i := 0; i < len(tgtHalf); i++ {
						tFull = append(tFull, int(tgtHalf[i]-'0'))
					}
					if odd && pos < m-1 {
						tFull = append(tFull, middle)
					}
					leftLen := m
					if odd {
						leftLen = m - 1
					}
					var mb strings.Builder
					for i := leftLen - 1; i >= 0; i-- {
						mb.WriteByte(byte('0' + tFull[i]))
					}
					if mb.String() > s[m:] {
						t = append(t, c)
						rem = r2
						placed = true
						break
					}
				}
			}
			if !placed {
				return -1
			}
		}
		// Every position stayed equal to s and the mirror check
		// passed, so t is complete and its palindrome beats s.
		var b strings.Builder
		for _, d := range t {
			b.WriteByte(byte('0' + d))
		}
		leftLen := m
		if odd {
			leftLen = m - 1
		}
		for i := leftLen - 1; i >= 0; i-- {
			b.WriteByte(byte('0' + t[i]))
		}
		v, _ := strconv.ParseInt(b.String(), 10, 64)
		return v
	}

	consider := func(subset []int) {
		L := 0
		for _, d := range subset {
			L += d
		}
		if L < digits {
			return
		}
		var halfCounts [10]int
		middle := -1
		for _, d := range subset {
			halfCounts[d] = d / 2
			if d%2 == 1 {
				middle = d
			}
		}
		if L > digits {
			var half []int
			for d := 1; d <= 9; d++ {
				for k := 0; k < halfCounts[d]; k++ {
					half = append(half, d)
				}
			}
			cand := smallestPalindrome(half, middle)
			if best < 0 || cand < best {
				best = cand
			}
		} else {
			cand := smallestHalfAbove(halfCounts, middle, L)
			if cand >= 0 && (best < 0 || cand < best) {
				best = cand
			}
		}
	}

	// Subsets of 1..9 with at most one odd digit.
	evens := []int{2, 4, 6, 8}
	odds := []int{1, 3, 5, 7, 9}
	for mask := 0; mask < 16; mask++ {
		var base []int
		for i := 0; i < 4; i++ {
			if mask&(1<<i) != 0 {
				base = append(base, evens[i])
			}
		}
		consider(base)
		for _, o := range odds {
			consider(append(append([]int{}, base...), o))
		}
	}
	return best
}
