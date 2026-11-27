# LeetCode 3451. Find Invalid IP Addresses — Hard
# https://leetcode.com/problems/find-invalid-ip-addresses/
# Submission 2202546788 — Accepted 10/10, Pandas (Python)
#
# My thinking: an address is valid only when it has exactly
# four octets, each 0-255 with no leading zeros, so one regex
# captures all three invalid rules at once. I keep the rows
# whose ip does not match it, count them per ip, and sort by
# the count then the ip, both descending.

import pandas as pd

_OCTET = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
_VALID_IP = rf"^({_OCTET}\.){{3}}{_OCTET}$"


def find_invalid_ip_addresses(logs: pd.DataFrame) -> pd.DataFrame:
    invalid = logs[~logs["ip"].str.match(_VALID_IP)]
    result = (
        invalid.groupby("ip", as_index=False)
        .size()
        .rename(columns={"size": "invalid_count"})
    )
    return result.sort_values(
        ["invalid_count", "ip"], ascending=[False, False]
    ).reset_index(drop=True)
