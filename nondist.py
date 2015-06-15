#!/usr/bin/env python2
# coding=utf-8
import random
import sys
import time
from fractions import gcd

if __name__ == "__main__":
    # Some general config
    numbers_count = int(sys.argv[1]) # liczba liczb do sprawdzenia NWD

    # Choose the numbers randomly
    numbers = []
    for x in range(0, numbers_count):
        numbers.append((int(sys.argv[2]) if len(sys.argv) > 2 else 1) * random.randint(1, (
        int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 12)))

    # print(numbers)

    start_time = time.time()
    # Reduce
    print("%s, %s" % (reduce(lambda x, y: gcd(x,y), numbers), (time.time() - start_time))) # 1st: GCD, 2nd: time of exec
