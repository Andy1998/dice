#! /usr/bin/env python

import library
import random

time = library.int_input("How many times do you want to roll >")
for x in range(0,time):
    side = library.int_input("How many sides do you want? >")
    num = random.randint(1,side)
    print num