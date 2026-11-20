# LeetCode 1797. Design Authentication Manager — Medium
# https://leetcode.com/problems/design-authentication-manager/
# Submission 2199935578 — Accepted, Python3
#
# My thinking: I keep each token's expiry
# time in a map. Generating sets it, renewing
# only works before it passes, and counting
# just checks how many expiries are still in
# the future.

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for expiry in self.tokens.values() if expiry > currentTime)
