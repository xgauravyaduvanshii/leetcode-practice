# LeetCode 736. Parse Lisp Expression — Hard
# https://leetcode.com/problems/parse-lisp-expression/
# Submission 2198670436 — Accepted, Python3
#
# My thinking: I split the expression into tokens and
# evaluate it recursively, carrying a scope of variable
# bindings. A let copies the scope, binds each variable
# in turn, then evaluates its body; add and mult just
# evaluate their two parts. A bare token is a number
# or a lookup in the current scope.

class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = self._tokenize(expression)
        pos = [0]

        def parse_expr(scope):
            token = tokens[pos[0]]
            pos[0] += 1
            if token == "(":
                op = tokens[pos[0]]
                pos[0] += 1
                if op == "let":
                    new_scope = dict(scope)
                    while True:
                        if tokens[pos[0]] == "(" or tokens[pos[0] + 1] == ")":
                            value = parse_expr(new_scope)
                            pos[0] += 1
                            return value
                        var = tokens[pos[0]]
                        pos[0] += 1
                        new_scope[var] = parse_expr(new_scope)
                first = parse_expr(scope)
                second = parse_expr(scope)
                pos[0] += 1
                return first + second if op == "add" else first * second
            if token.lstrip("-").isdigit():
                return int(token)
            return scope[token]

        return parse_expr({})

    def _tokenize(self, expression):
        tokens = []
        current = ""
        for ch in expression:
            if ch in "()":
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(ch)
            elif ch == " ":
                if current:
                    tokens.append(current)
                    current = ""
            else:
                current += ch
        if current:
            tokens.append(current)
        return tokens
