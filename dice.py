#! /usr/bin/env python
import library
import random
side = library.int_input("How many sides do you want? >")
time = library.int_input("How many times do you want to roll >")
for x in range(1,time):
    num = random.randint(1,side)
    print num