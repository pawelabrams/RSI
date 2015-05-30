#!/usr/bin/env python2
# coding=utf-8
import random
import sys
import time
from fractions import gcd

if __name__ == "__main__":
    start_time = time.time()
    port_number = int(sys.argv[3]) if len(sys.argv) > 3 else 9500
    machine_count = int(sys.argv[1])  # liczba maszyn
    numbers_count = int(sys.argv[2])  # liczba liczb do sprawdzenia NWD

    numbers = []
    for x in range(0, numbers_count):
        numbers.append((int(sys.argv[4]) if len(sys.argv) > 4 else 1) * random.randint(1, (
        int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 12)))

    print(numbers)

    # one last reduce:

    print("The GCD of those is: %s" % reduce(lambda x, y: gcd(x, y), numbers))

    print("--- %s seconds ---" % (time.time() - start_time))
