#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    def summ(*args):
        if args:
            values = [int(arg) for arg in args]
            print(values)
            imin = 0
            minval = int(values[0])
            for i in range(len(values)):
                if values[i] < minval:
                    minval = values[i]
                    imin = i
            imin += 1
            sum = 0
            for i in range(imin, len(values)):
                sum += abs(values[i])
            return sum
        else:
            return None

print("сумма ", summ(3, 7, 1, -3, 2, 6, 0, 5))
