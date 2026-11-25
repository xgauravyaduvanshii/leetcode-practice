# LeetCode 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target — Hard
# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
# Submission 2203137064 — Accepted, Python3


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        # My thinking: a palindrome is fixed by its first half
        # plus at most one odd middle character, so more than one
        # odd frequency means no palindrome exists at all. The
        # smallest palindrome above target either matches target's
        # first half exactly (then the mirror decides whether it
        # is greater), or it matches target's first half up to
        # some position, puts the smallest bigger character there,
        # and fills the rest with the smallest characters left.
        # Trying the exact match first, then the split positions
        # from right to left, gives the smallest answer, since a
        # later split keeps a longer prefix of target.
        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        odd = 0
        middle = ""
        for i in range(26):
            if freq[i] % 2 == 1:
                odd += 1
                middle = chr(97 + i)
        if odd > 1:
            return ""
        half = [v // 2 for v in freq]
        half_len = n // 2
        target_half = target[:half_len]

        def build(left: str) -> str:
            right = left[::-1]
            if n % 2:
                return left + middle + right
            return left + right

        # Exact case: the first half equals target's first half.
        rem = half[:]
        matched = True
        for i in range(half_len):
            x = ord(target_half[i]) - 97
            if rem[x] == 0:
                matched = False
                break
            rem[x] -= 1
        if matched:
            cand = build(target_half)
            if cand > target:
                return cand
        # Split cases: match target's first half up to pos, then
        # raise the character at pos and take the smallest rest.
        for pos in range(half_len - 1, -1, -1):
            rem = half[:]
            ok = True
            for i in range(pos):
                x = ord(target_half[i]) - 97
                if rem[x] == 0:
                    ok = False
                    break
                rem[x] -= 1
            if not ok:
                continue
            target_char = ord(target_half[pos]) - 97
            for c in range(target_char + 1, 26):
                if rem[c] > 0:
                    left = target_half[:pos] + chr(97 + c)
                    rem[c] -= 1
                    for x in range(26):
                        left += chr(97 + x) * rem[x]
                    cand = build(left)
                    if cand > target:
                        return cand
                    break
        return ""
