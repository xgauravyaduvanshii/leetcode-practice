# LeetCode 535. Encode and Decode TinyURL — Medium
# https://leetcode.com/problems/encode-and-decode-tinyurl/
# Submission 2198852340 — Accepted, Python3
#
# My thinking: a counter gives every long URL its
# own short key, and a dictionary remembers which
# key belongs to which URL. Encoding hands out the
# next key; decoding looks it up again.

class Codec:
    def __init__(self):
        self.urls = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        key = str(self.counter)
        self.urls[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.rsplit("/", 1)[-1]
        return self.urls[key]
