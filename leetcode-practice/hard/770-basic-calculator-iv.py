from collections import Counter


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: list[str], evalvals: list[int]) -> list[str]:
        # My thinking: keep every term as a monomial — a sorted tuple
        # of variables — with its coefficient; addition merges equal
        # monomials, multiplication merges the variable lists, and
        # evaluation substitutes values where it can.
        eval_map = dict(zip(evalvars, evalvals))
        tokens = []
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch == " ":
                i += 1
            elif ch in "+-*()":
                tokens.append(ch)
                i += 1
            elif ch.isdigit():
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                tokens.append(int(expression[i:j]))
                i = j
            else:  # variable (letters, possibly multi-letter)
                j = i
                while j < len(expression) and expression[j].isalpha():
                    j += 1
                tokens.append(expression[i:j])
                i = j
        pos = [0]

        def add(p, q, sign):
            out = Counter(p)
            for mono, coeff in q.items():
                out[mono] += sign * coeff
            return {m: c for m, c in out.items() if c != 0}

        def mul(p, q):
            out = Counter()
            for m1, c1 in p.items():
                for m2, c2 in q.items():
                    out[tuple(sorted(m1 + m2))] += c1 * c2
            return {m: c for m, c in out.items() if c != 0}

        def parse_expr():
            result = parse_term()
            while pos[0] < len(tokens) and tokens[pos[0]] in ("+", "-"):
                op = tokens[pos[0]]
                pos[0] += 1
                term = parse_term()
                result = add(result, term, 1 if op == "+" else -1)
            return result

        def parse_term():
            result = parse_factor()
            while pos[0] < len(tokens) and tokens[pos[0]] == "*":
                pos[0] += 1
                factor = parse_factor()
                result = mul(result, factor)
            return result

        def parse_factor():
            tok = tokens[pos[0]]
            pos[0] += 1
            if tok == "(":
                result = parse_expr()
                pos[0] += 1  # skip ")"
                return result
            if isinstance(tok, int):
                return {(): tok}
            if tok in eval_map:
                return {(): eval_map[tok]}
            return {(tok,): 1}

        poly = parse_expr()
        terms = sorted(poly.items(), key=lambda kv: (-len(kv[0]), kv[0]))
        result = []
        for mono, coeff in terms:
            if mono:
                result.append(str(coeff) + "*" + "*".join(mono))
            else:
                result.append(str(coeff))
        return result
