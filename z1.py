#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    def midlgeom(a):
        if len(a) != 0:
            res = 1
            for i in range(len(a)):
                res *= a[i]
            return pow(res, 1 / (len(a)))
        else:
            return None

raw = input('Введите последовательность чисел через пробел: ')
mas = [int(i) for i in raw.split(' ') if i.isdigit()]

print(midlgeom(mas))
