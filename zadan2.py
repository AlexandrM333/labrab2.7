#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    while True:
        slovo1 = set(input("Введите 1-oe слово: "))
        slovo2 = set(input("Введите 2-oe слово: "))
        simv = slovo1.intersection(slovo2)

        if simv == set():
            print("Нет одинаковых символов")
        else:
            print("Одинаковые символы: ", simv)
