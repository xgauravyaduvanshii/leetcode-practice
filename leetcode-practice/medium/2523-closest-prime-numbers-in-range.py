class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        # My thinking: sieve up to right once to mark the primes, then walk
        # the primes inside [left, right] and keep the pair with the
        # smallest gap (ties keep the earlier pair, since we only replace
        # on a strictly smaller gap).
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False
        prev = -1
        best = [-1, -1]
        best_gap = right - left + 1
        for x in range(left, right + 1):
            if is_prime[x]:
                if prev != -1 and x - prev < best_gap:
                    best_gap = x - prev
                    best = [prev, x]
                prev = x
        return best
