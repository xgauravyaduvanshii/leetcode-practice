class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # My thinking: parse the string like a tiny grammar —
        # commas union sets, neighbours multiply them — and let
        # the recursion handle the nesting.
        n = len(expression)
        pos = 0

        def parse_expr():
            nonlocal pos
            result = parse_term()
            while pos < n and expression[pos] == ",":
                pos += 1
                result |= parse_term()
            return result

        def parse_term():
            nonlocal pos
            result = {""}
            while pos < n and expression[pos] not in ",}":
                factor = parse_factor()
                result = {a + b for a in result for b in factor}
            return result

        def parse_factor():
            nonlocal pos
            if expression[pos] == "{":
                pos += 1
                result = parse_expr()
                pos += 1  # skip '}'
                return result
            ch = expression[pos]
            pos += 1
            return {ch}

        return sorted(parse_expr())
