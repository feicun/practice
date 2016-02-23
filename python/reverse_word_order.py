#!/usr/bin/env python
# encoding: utf-8


def reverse_word():
    s = "My name is Haoming haha"
    result = " ".join(s.split()[::-1])
    print result
    return result

reverse_word()
