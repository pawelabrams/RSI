#!/usr/bin/env python2
# coding=utf-8
import random
import sys
import time
import Pyro4 as pyro

if __name__ == "__main__":
    start_time = time.time()
    port_number = 9601
    machine_count = int(sys.argv[1]) # liczba maszyn
    numbers_count = int(sys.argv[2]) # liczba liczb do sprawdzenia NWD

	servers = ['PYRO:dg@localhost:9500']
	block_size = int(numbers_count/machine_count)
