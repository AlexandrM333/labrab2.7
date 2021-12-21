#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"a", "e", "f", "i"}
    B = {"a", "b", "k", "n"}
    C = {"e", "f", "n", "o", "w", "x"}
    D = {"a", "d", "e", "o", "p", "t" "u"}

    ab1 = A.union(B)
    X = ab1.intersection(C)
    print(f"X = {X}")

    nea = u.difference(A)
    neb = u.difference(B)
    ab2 = nea.intersection(neb)
    cd = C.union(D)
    Y = ab2.difference(cd)
    print(f"Y = {Y}")
