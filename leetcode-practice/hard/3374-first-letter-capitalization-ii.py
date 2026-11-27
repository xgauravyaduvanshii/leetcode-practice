# LeetCode 3374. First Letter Capitalization II — Hard
# https://leetcode.com/problems/first-letter-capitalization-ii/
# Submission 2202488789 — Accepted 15/15, Pandas
#
# My thinking: a word that starts with a non-letter is left alone. A word
# made of two or more all-letter parts joined by hyphens gets the first
# letter of every part capitalised and the rest lowered. Any other word just
# gets its first letter capitalised and every other letter lowered. Matching
# on runs of non-spaces keeps every space exactly where it was.

import re

import pandas as pd


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def convert_word(word):
        if not word or not word[0].isalpha():
            return word
        if re.fullmatch(r"[A-Za-z]+(?:-[A-Za-z]+)+", word):
            return "-".join(
                part[:1].upper() + part[1:].lower() for part in word.split("-")
            )
        return word[:1].upper() + "".join(
            ch.lower() if ch.isalpha() else ch for ch in word[1:]
        )

    result = user_content.copy()
    result["original_text"] = result["content_text"]
    result["converted_text"] = result["content_text"].apply(
        lambda text: re.sub(r"\S+", lambda m: convert_word(m.group(0)), text)
    )
    return result[["content_id", "original_text", "converted_text"]]
