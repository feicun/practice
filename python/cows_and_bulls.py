#!/usr/bin/env python
# encoding: utf-8

import random

def compare_number(number, user_guess):
    cow = 0
    bull = 0
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            cow += 1
        else:
            bull += 1
    return cow, bull

if __name__ ==  "__main__":
    playi
