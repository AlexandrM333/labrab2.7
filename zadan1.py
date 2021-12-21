#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glasnie = set("аеёиоуыэюяaeiouy")

    while True:
        word = list(input("Введите слово: "))
        x = 0
        for i in word:
            if i in glasnie:
                x += 1

        print(x)
