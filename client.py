# coding=utf-8
import random
import sys
import time
import Pyro4 as pyro

if __name__ == "__main__":
    start_time = time.time()
    port_number = 9601
    machineNumber = float(sys.argv[1])
    machineNumber = math.sqrt(machineNumber)
    array_size = int(sys.argv[2])
    if machineNumber.is_integer() and array_size % machineNumber == 0:
        client = ClientClass()
        client.run(machineNumber, port_number, int(sys.argv[3]), int(sys.argv[4]))
    else:
        print('Square root of machines count must be an integer!')
