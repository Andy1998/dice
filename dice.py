#! /usr/bin/env python
import library
import random
side = library.int_input("How many sides do you want? >")
while side < 2:
    side = library.int_input("The dice should have at least one side. Try again >")
time = library.int_input("How many times do you want to roll >")
for x in range(1,time):
    num = random.randint(1,side)
    print num