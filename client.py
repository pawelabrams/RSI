#!/usr/bin/env python2
# coding=utf-8
import random
import sys
import time
from math import ceil
from fractions import gcd
import Pyro4 as pyro

if __name__ == "__main__":
    start_time = time.time()
    port_number = int(sys.argv[3]) if len(sys.argv) > 3 else 9500
    machine_count = int(sys.argv[1]) # liczba maszyn
    numbers_count = int(sys.argv[2]) # liczba liczb do sprawdzenia NWD

    numbers = []
    for x in range(0, numbers_count):
        numbers.append((int(sys.argv[4]) if len(sys.argv) > 4 else 1) * random.randint(1, (int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 12)))

    print(numbers)

    servers = ['PYRO:dg@localhost:']
    block_size = int(ceil(numbers_count/machine_count))
    block_count = int(ceil(numbers_count/block_size))

    machine_no = 0
    srv_array = []
    for y in range(0, block_count):
        url = servers[machine_no % len(servers)] + str(port_number)
        dg = pyro.Proxy(url)
        dg.setls(numbers[machine_no*block_size:(machine_no+1)*block_size])
        srv_array.append(dg)
        machine_no += 1
        if machine_no % len(servers) == 0:
            port_number += 1

    for element in srv_array:
        element.dgcd()

    one_last_reduce = []
    for element in srv_array:
        one_last_reduce.append(element.getret())

    # one last reduce:

    print("The GCD of those is: %s" % reduce(lambda x, y: gcd(x,y), one_last_reduce))

    print("--- %s seconds ---" % (time.time() - start_time))
