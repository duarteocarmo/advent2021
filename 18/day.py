from math import prod, floor, ceil
from functools import lru_cache, reduce
from copy import copy
from pprint import pprint
from collections import defaultdict, Counter
from math import prod
import sys

sys.setrecursionlimit(10 ** 6)

with open("18/input.txt") as f:
    txt = f.read()


class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"{self.val}"

    def __eq__(self, other):
        if type(other) == Node:
            return self.val == other.val
        return False

    def __hash__(self):
        return hash(self.val)


flatten = lambda l: sum(map(flatten, l), []) if type(l) == tuple else [l]


def to_ast(ast):
    if type(ast) == int:
        return Node(ast)
    l, r = ast
    return (to_ast(l), to_ast(r))


def explode(ast):
    i = 0
    flat = flatten(ast)
    done = False

    def explode_aux(ast, flat, depth=0):
        nonlocal i, done
        if type(ast) == Node:
            i += 1
            return ast
        l, r = ast
        if type(l) == Node and type(r) == Node:
            if depth > 3 and not done:
                if i > 0:
                    flat[i - 1].val += flat[i].val
                if i + 1 < len(flat) - 1:
                    flat[i + 2].val += flat[i + 1].val
                done = True
                return Node(0)
        return (explode_aux(l, flat, depth + 1), explode_aux(r, flat, depth + 1))

    return explode_aux(ast, flat)


def split(ast):
    splitted = False

    def split_aux(ast):
        nonlocal splitted
        if type(ast) == Node:
            if ast.val >= 10 and not splitted:
                splitted = True
                return (Node(floor(ast.val / 2)), Node(ceil(ast.val / 2)))
            return ast
        l, r = ast
        return (split_aux(l), split_aux(r))

    return split_aux(ast)


def magnitude(ast):
    if type(ast) == Node:
        return ast.val
    l, r = ast
    return 3 * magnitude(l) + 2 * magnitude(r)


def calc(lines):
    ast = to_ast(eval(lines[0]))
    read = 0
    while True:
        while True:
            new = explode(ast)
            if ast != new:
                ast = new
                continue
            new = split(ast)
            if ast != new:
                ast = new
                continue
            break
        read += 1
        if read == len(lines):
            break
        line = lines[read]
        ast = (ast, to_ast(eval(line)))
    return magnitude(ast)


def p1():
    print(calc(tuple(txt.splitlines())))


def p2():
    def c():
        lines = txt.splitlines()
        for i, a in enumerate(lines):
            for j, b in enumerate(lines):
                if i != j:
                    yield calc((a, b))

    print(max(c()))


p1()
p2()
