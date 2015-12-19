#!/usr/bin/env python
# encoding: utf-8

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p = "".join(random.sample(s, passlen))
print p
